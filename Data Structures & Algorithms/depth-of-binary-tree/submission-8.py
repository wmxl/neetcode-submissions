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
        q.append(root)
        cur_num = 1
        d = 1
        while q:
            if cur_num == 0:
                cur_num = len(q)
                d += 1
            cur = q.popleft() 
            cur_num -= 1
            if cur.left: 
                q.append(cur.left)
            if cur.right: 
                q.append(cur.right)
        return d