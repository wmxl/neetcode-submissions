# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # firstly find every node's max value from this node to outest leaf
        # must inlucde this node but don't have to include left or right
        dfs_dict = {}
        def dfs(root):
            if root is None:
                return 0
            if root in dfs_dict:
                return dfs_dict[root]
            max_left = dfs(root.left)
            max_right = dfs(root.right)
            ans = root.val + max(max_left, max_right, 0)
            dfs_dict[root] = ans
            return ans
        dfs(root)

        # traverse tree and find subtree's max path sum in current node as root
        max_ans = float('-inf')
        def maxsum(root):
            if root is None:
                return 0
            ans = root.val + max(dfs(root.left), 0) + max(dfs(root.right), 0)
            nonlocal max_ans 
            max_ans = max(max_ans, ans)
            maxsum(root.left)
            maxsum(root.right)
        maxsum(root)
        
        return max_ans
