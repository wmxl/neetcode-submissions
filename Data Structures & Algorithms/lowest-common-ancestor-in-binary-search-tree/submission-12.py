# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, r: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        print(f"r:{r.val}")
        f = self.lowestCommonAncestor
        if r.val > p.val and r.val > q.val:
            print(1)
            return f(r.left, p, q)
        elif r.val < p.val and r.val < q.val:
            print(2)
            return f(r.right, p, q)
        else:
            print(r.val)
            return r



        