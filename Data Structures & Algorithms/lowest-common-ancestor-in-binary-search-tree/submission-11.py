# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        cur = root
        while cur:
            if cur.val == p.val or cur.val == q.val:
                return cur
            
            if (cur.val > p.val and cur.val < q.val) or (cur.val < p.val and cur.val > q.val):
                return cur
            
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            else:
                cur = cur.right





        # if root.val == p.val or root.val == q.val:
        #     return root
        
        # if (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val):
        #     return root
        
        # if root.val > p.val and root.val > q.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        
        # else:
        #     return self.lowestCommonAncestor(root.right, p, q)

        