# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def _traverse(n):
            if n is None:
                return
            if n.left: _traverse(n.left)
            if n.right: _traverse(n.right)
            res.append(n.val)
        _traverse(root)
        return res