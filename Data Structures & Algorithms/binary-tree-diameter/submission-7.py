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
            if not root: return 0
            if root in d:
                return d[root]
            depth = max(maxDepth(root.left), maxDepth(root.right)) + 1
            d[root] = depth
            return depth

        def visit(root):
            nonlocal ma
            if not root: return

            ma = max(ma, (d[root.left] if root.left else 0) + (d[root.right] if root.right else 0))
            visit(root.left)
            visit(root.right)
        
        maxDepth(root)
        visit(root)
        return ma


        

        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    