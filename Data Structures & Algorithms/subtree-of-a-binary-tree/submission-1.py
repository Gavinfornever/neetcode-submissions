# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self, l, r):
        if not l and (not r):return True
        if (not l and r) or (l and (not r)):return False
        if l.val == r.val and \
            self.isSame(l.left, r.left) and \
            self.isSame(l.right, r.right):
            return True
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = self.isSame(root, subRoot)
        if root.left:
            res = res or self.isSubtree(root.left, subRoot)
        if root.right:
            res = res or self.isSubtree(root.right, subRoot)
        
        return res
        
        



