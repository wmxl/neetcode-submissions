# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ma = root.val if root else 0
        cnt = 0

        def good(r, ma):
            nonlocal cnt 
            if not r:
                return 
            if r.val >= ma:
                cnt += 1
                ma = r.val
            good(r.left, ma)
            good(r.right, ma)
        
        good(root, ma)

        return cnt

