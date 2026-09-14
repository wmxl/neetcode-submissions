# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        idof = {}
        def visit(root):
            if not root: return 0
            left_id = visit(root.left)
            if left_id == -1: return -1
            right_id = visit(root.right)
            if right_id == -1: return -1
            
            key = (left_id, root.val, right_id)
            if key not in idof:
                idof[key] = len(idof) + 1
            if idof[key] == subRoot_id:
                return -1
            return idof[key]

        subRoot_id = -2
        subRoot_id = visit(subRoot)

        return visit(root) == -1

        
        
        