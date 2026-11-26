# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        stack = [(root, False)]
        heights = {}

        while stack:
            node, visited = stack.pop()

            if not node:
                continue
            
            if visited:
                left = heights.get(node.left, 0)
                right = heights.get(node.right, 0)
                if abs(left - right) > 1:
                    return False
                heights[node] = 1 + max(left, right)
            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
        return True



        # def dfs(node):
        #     if not node:
        #         return [True, 0]
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

        #     return [balanced, 1 + max(left[1], right[1])]
        
        # return dfs(root)[0]

        # def height(node):
        #     if not node:
        #         return 0
            
        #     left = height(node.left)
        #     right = height(node.right)

        #     if left == -1 or right == -1:
        #         return -1

        #     if abs(left - right) > 1:
        #         return -1
            
        #     return 1 + max(left, right)
        
        # return height(root) != -1
        
    
        