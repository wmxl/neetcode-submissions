# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        fast = head
        slow = head
        while slow and fast:
            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next.next
            if fast == slow:
                return True
        return False

        