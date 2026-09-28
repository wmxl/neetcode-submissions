# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def smallest(r):
            nonlocal k
            print(f'k:{k}')
            if r.left:
                smallest(r.left)
            print(r.val)
            k -= 1
            if k == 0:
                self.ans = r.val
            if r.right:
                smallest(r.right)

        smallest(root)
        return self.ans
        