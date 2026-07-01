# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMax(self, root):
        res = -10000
        if not root:return res
        res = root.val
        if root.left: res = max(res, self.getMax(root.left))
        if root.right: res = max(res, self.getMax(root.right))
        return res
    
    def getMin(self, root):
        res = -10000
        if not root:return res
        res = root.val
        if root.left: res = min(res, self.getMax(root.left))
        if root.right: res = min(res, self.getMax(root.right))
        return res

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:return True
        if root.left and self.getMax(root.left) >= root.val:return False
        if root.right and self.getMin(root.right) <= root.val:return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
