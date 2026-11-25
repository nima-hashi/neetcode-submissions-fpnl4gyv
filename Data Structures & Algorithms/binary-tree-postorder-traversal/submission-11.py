# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = [root]
        visit = [False]
        res = []

        while stack:
            cur, v = stack.pop(), visit.pop()
            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visit.append(True)
                    if cur.right:
                        stack.append(cur.right)
                        visit.append(False)
                    if cur.left:
                        stack.append(cur.left)
                        visit.append(False)
        return res


        # if not root:
        #     return []

        # stack = [root]
        # result = []

        # while stack:
        #     node = stack.pop()
        #     result.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return result[::-1]



        # result = []

        # def dfs(node):
        #     if not node:
        #         return []
        #     dfs(node.left)
        #     dfs(node.right)
        #     result.append(node.val)
        
        # dfs(root)
        # return result
        