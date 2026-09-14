# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if root:
            q.append(root)
        output = []
        while q:
            cnt = len(q)
            while cnt > 0:
                cnt -= 1
                r = q.popleft()
                if cnt == 0:
                    output.append(r.val)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
        return output
        