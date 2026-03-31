# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return

        head = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return head

        headInd = inorder.index(preorder[0])
        head.left = self.buildTree(preorder[1:1+headInd], inorder[:headInd])
        head.right = self.buildTree(preorder[headInd+1:], inorder[headInd+1:])

        return head


        