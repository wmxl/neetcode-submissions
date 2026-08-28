# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        l = ListNode(0)
        p = l
        jin = False
        while p1 or p2:
            if p1 and p2:
                val = p1.val + p2.val
            elif p1:
                val = p1.val
            elif p2:
                val = p2.val
            else:
                val = 0

            if jin:
                val += 1

            if val >= 10:
                jin = True
                val = val % 10
            else:
                jin = False
            
            p.next = ListNode(val)
            p = p.next

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        if jin:
            p.next = ListNode(1)
        return l.next
                
                
