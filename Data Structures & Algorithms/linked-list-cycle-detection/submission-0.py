# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head
        d = {}
        while p:
            if p not in d:
                d[p] = 1
            else:
                return True
            p = p.next
        return False

        