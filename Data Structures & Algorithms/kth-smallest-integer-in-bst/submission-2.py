# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        c = 0

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            popped = stack.pop()
            c += 1
            if c == k:
                return popped.val
            root = popped.right
        return 
        