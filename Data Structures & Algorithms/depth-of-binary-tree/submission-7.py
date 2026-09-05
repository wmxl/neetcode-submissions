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
        next_num = 0
        d = 1
        while q:
            cur = q.popleft() 
            if cur_num == 0:
                cur_num = next_num
                next_num = 0
                d += 1
            cur_num -= 1
            if cur.left: 
                q.append(cur.left)
                next_num += 1
            if cur.right: 
                q.append(cur.right)
                next_num += 1
        return d