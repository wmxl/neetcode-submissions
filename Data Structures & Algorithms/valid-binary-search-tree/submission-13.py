# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inf = 9999999
        def f(r):
            nonlocal inf
            if not r:
                return (-inf,True,inf)
            
            left = f(r.left)
            right = f(r.right)

            if (not left[1]) or (not right[1]):
                return (-inf, False, inf)
 
            if left[0] < r.val < right[2]:
                # print((right[0], True, left[2]))
                ma = max(r.val, right[0])
                mi = min(r.val, left[2])
                return (ma, True, mi)
            else:
                return (-inf, False, inf)

        m = f(root)
        print(m)
        return m[1]
            
        