# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        l3 = ListNode()
        p3 = l3
        while p1 or p2:
            if p1 is None:
                p3.next = p2
                p2 = p2.next
            elif p2 is None:
                p3.next = p1
                p1 = p1.next
            elif p1.val > p2.val:
                p3.next = p2
                p2 = p2.next
            else:
                p3.next = p1
                p1 = p1.next

            p3 = p3.next

        return l3.next
        
            

        