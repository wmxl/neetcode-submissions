# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_d = {}
        n = len(inorder)
        for i in range(n):
            in_d[inorder[i]] = i

        def bt(pre_left, leng, in_left):
            if leng == 0:
                return None
            root_num = preorder[pre_left]
            root_pos = in_d[root_num]
            new_len = root_pos - in_left
            root = TreeNode(root_num)
            root.left = bt(pre_left+1, new_len, in_left)
            root.right = bt(pre_left+new_len+1, leng-new_len-1, root_pos+1)    
            return root
        return bt(0,n,0)

