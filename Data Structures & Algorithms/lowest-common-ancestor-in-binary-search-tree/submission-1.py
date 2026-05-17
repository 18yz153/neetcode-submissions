# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(root):
            if not root:
                return None
            if root.val == p.val:
                return p
            if root.val == q.val:
                return q
            
            foundleft = dfs(root.left)
            foundright = dfs(root.right)
            if foundleft and foundright:
                return root
            elif foundleft:
                return foundleft
            else:
                return foundright
        return dfs(root)