# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if root:
            q.append(root)
        output = []
        while q:
            cnt = len(q)
            layer = []
            while cnt > 0:
                cnt -= 1
                r = q.popleft()
                layer.append(r.val)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            output.append(layer)
        return output
