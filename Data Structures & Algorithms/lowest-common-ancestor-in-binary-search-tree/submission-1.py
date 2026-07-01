# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        x = root

        while x:
            if p.val<x.val and q.val<x.val:
                x = x.left
            elif p.val>x.val and q.val>x.val:
                x = x.right
            elif p.val == x.val or q.val == x.val:
                return x
            elif p.val>x.val and q.val<x.val:
                return x
            elif p.val<x.val and q.val>x.val:
                return x

        # lp, lq = [], []
        # x = root
        # while x:
        #     lp.append(x.val)
        #     if p.val<x:
        #         x = x.left
        #     elif p.val>x:
        #         x = x.right
        #     else:
        #         break
        
        # x = root
        # while x:
        #     lq.append(x.val)
        #     if q.val<x:
        #         x = x.left
        #     elif q.val>x:
        #         x = x.right
        #     else:
        #         break
        
        # l, r = 0, 0
        # while l<len(lp) and r<len(lq):







