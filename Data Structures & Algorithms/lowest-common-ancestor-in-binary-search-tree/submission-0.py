# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        x = root
        while( x ):
            if (p.val<x.val and q.val>x.val) or \
               (p.val>x.val and q.val<x.val):
                return x
            elif p.val==x.val:
                return p
            elif q.val == x.val:
                return q
            elif p.val<x.val and q.val <x.val:
                x = x.left
            else:
                x = x.right
        return x