# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values = to_list(root)
        values = [str(x) for x in values]
        s = "#".join(values)
        # print(f"serialize: {s}")
        return s

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        values = data.split("#")
        values = [int(x) if x != "None" else None for x in values]
        # print(f"deserialize: {values}")
        return build(values)


def build(nums: List[Optional[int]]) -> Optional[TreeNode]:
    if not nums:
        return None
    root = TreeNode(nums[0])
    q = deque([root])
    i = 1
    while q and i < len(nums):
        node = q.popleft()
        if i < len(nums) and nums[i] is not None:
            node.left = TreeNode(nums[i])
            q.append(node.left)
        i += 1
        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            q.append(node.right)
        i += 1
    return root


def to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    q = deque([root])
    out: List[Optional[int]] = []
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out