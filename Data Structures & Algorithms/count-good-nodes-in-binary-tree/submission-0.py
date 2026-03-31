# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, m):
            res = 0
            if not node:
                return 0
            
            if node.val >= m:
                res += 1
            
            res += dfs(node.left, max(m, node.val))
            res += dfs(node.right, max(m, node.val))

            return res

        return dfs(root, root.val)