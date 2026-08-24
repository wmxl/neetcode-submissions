# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head1 = ListNode()
        head1.next = head

        p1 = head1
        p = head
        while n > 0:
            p = p.next
            n -= 1
        while p:
            p = p.next
            p1 = p1.next

        p1.next = p1.next.next
        return head1.next
            