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
        d = 0
        while q:
            layer_num = len(q)
            while layer_num > 0:
                cur = q.popleft() 
                if cur.left: 
                    q.append(cur.left)
                if cur.right: 
                    q.append(cur.right)
                layer_num -= 1
            d += 1
        return d