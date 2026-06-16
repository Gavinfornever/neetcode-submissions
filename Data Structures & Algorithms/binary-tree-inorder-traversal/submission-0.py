# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def _traverse(n):
            if n is None:
                return
            if n.left: _traverse(n.left)
            res.append(n.val)
            if n.right: _traverse(n.right)
        _traverse(root)
        return res
        
