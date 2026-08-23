# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head)
        if head == None or head.next == None:
            return head

        l, m, r = head, head.next, head.next.next

        while True:
            # print(m)
            if l == head:
                l.next = None
            m.next = l
            l = m
            if r == None:
                break
            m = r
            r = r.next
        return m