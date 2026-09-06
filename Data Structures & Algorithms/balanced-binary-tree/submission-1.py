# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        ma = True

        def maxDepth(root):
            nonlocal ma
            if not root: return 0
            
            maxdepth_left = maxDepth(root.left)
            maxdepth_right = maxDepth(root.right)

            if maxdepth_left > maxdepth_right:
                if maxdepth_left - maxdepth_right > 1:
                    ma = False
            else:
                if maxdepth_right - maxdepth_left > 1:
                    ma = False

            return max(maxdepth_left, maxdepth_right) + 1
        maxDepth(root)
        return ma