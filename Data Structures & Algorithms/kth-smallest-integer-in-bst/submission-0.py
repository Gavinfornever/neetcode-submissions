# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self,):
        self.nums = []

    def firstTraverse(self, root):
        if not root:return
        if root.left: 
            self.firstTraverse(root.left)
        self.nums.append(root.val)
        if root.right:
            self.firstTraverse(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.firstTraverse(root)
        return self.nums[k-1]
