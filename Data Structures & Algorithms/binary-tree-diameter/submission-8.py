# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = {}
        ma = 0

        def maxDepth(root):
            nonlocal ma
            if not root: return 0
            
            maxdepth_left = maxDepth(root.left)
            maxdepth_right = maxDepth(root.right)
            ma = max(ma,  maxdepth_left + maxdepth_right)
            return max(maxdepth_left, maxdepth_right) + 1

        maxDepth(root)
        return ma


        

        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    