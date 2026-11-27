# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = [root]
        hm = {None: (0,0)} # height, diameter

        while stack:
            node = stack[-1]
            if node.left and node.left not in hm:
                stack.append(node.left)
            elif node.right and node.right not in hm:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftHeight, leftDiameter = hm[node.left]
                rightHeight, rightDiameter = hm[node.right]
                hm[node] = (1 + max(leftHeight, rightHeight), max(leftHeight + rightHeight, leftDiameter, rightDiameter))



        return hm[root][1]






        # diameter = 0

        # def dfs(node):

        #     nonlocal diameter

        #     if not node:
        #         return 0
            
        #     left = dfs(node.left)
        #     right = dfs(node.right)

        #     diameter = max(diameter, left + right)

        #     return 1 + max(left, right)
        
        # dfs(root)
        # return diameter


        