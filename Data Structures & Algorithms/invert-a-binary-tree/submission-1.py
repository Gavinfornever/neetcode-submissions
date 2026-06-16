# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _invert(p):
            if p is None:return
            if p.left or p.right:
                tmp = p.left if p.left else None
                p.left = p.right if p.right else None
                p.right = tmp
                _invert(p.left)
                _invert(p.right)
            return
        _invert(root)
        return root
