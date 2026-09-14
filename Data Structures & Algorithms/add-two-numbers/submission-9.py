# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode(0)
        p1, p2, p = l1, l2, l
    
        jin = 0
        while p1 or p2:
            if p1 and p2:
                val = p1.val + p2.val
            elif p1:
                val = p1.val
            else:
                val = p2.val

            val += jin

            jin = val // 10
            val = val % 10
            
            p.next = ListNode(val)
            p = p.next

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        if jin != 0:
            p.next = ListNode(1)
        return l.next
                
                
