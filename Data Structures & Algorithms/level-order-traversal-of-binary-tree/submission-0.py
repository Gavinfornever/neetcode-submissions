# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        res = []
        q = []
        q.append((root, 1))
        while q:
            x, depth = q.pop()
            if len(res)<depth:
                res.append([x.val])
            else:
                res[depth-1].append(x.val)
            if x.right: q.append((x.right,depth+1))
            if x.left: q.append((x.left,depth+1))
        
        return res