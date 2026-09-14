# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0 
        q = deque()
        ma = root.val = 1
        q.append(root)
        while q:
            cur = q.popleft() 
            cur_depth = cur.val
            if cur.left: 
                cur.left.val = cur_depth + 1
                q.append(cur.left)
                ma = max(cur.left.val, ma)
            if cur.right: 
                cur.right.val = cur_depth + 1
                q.append(cur.right)
                ma = max(cur.right.val, ma)
        return ma