# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validBST(self, root, left, right):
        if not root:
            return True
        if root.val <= left or root.val >= right:
            return False
        L = self.validBST(root.left, left, root.val)
        R = self.validBST(root.right, root.val, right)

        if not L or not R:
            return False
        
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBST(root,float('-inf'), float('inf'))
        
        