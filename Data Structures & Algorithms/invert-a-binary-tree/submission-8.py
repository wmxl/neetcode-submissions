# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft() 
            print(q)
            print(cur)
            left = cur.left
            right = cur.right
            cur.left = right
            cur.right = left
            left, right = right, left
            if left: q.append(left)
            if right: q.append(right)
        return root
