# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def search(root):
            nonlocal res
            if not root:
                return 0
            leftheight = search(root.left)+1
            rightheight = search(root.right)+1
            if abs(leftheight - rightheight) >1:
                res = False
            return max(leftheight,rightheight)

        search(root)
        return res