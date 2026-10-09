# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_d, pr_d = {}, {}
        n = len(inorder)
        for i in range(n):
            in_d[inorder[i]] = i
            pr_d[preorder[i]] = i

        def bt(pre_left, pre_right, in_left, in_right):
            if pre_left == pre_right:
                return None
            root_num = preorder[pre_left]
            root_pos = in_d[root_num]
            new_len = root_pos - in_left
            root = TreeNode(root_num)
            root.left = bt(pre_left+1, pre_left+new_len+1, in_left, root_pos)
            root.right = bt(pre_left+new_len+1, pre_right, root_pos+1, in_right)    
            return root
        return bt(0,n,0,n)

