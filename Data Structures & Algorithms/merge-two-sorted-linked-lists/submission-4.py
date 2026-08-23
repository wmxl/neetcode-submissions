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
                val = p2.val
                p2 = p2.next
            elif p2 is None:
                val = p1.val
                p1 = p1.next
            elif p1.val > p2.val:
                val = p2.val
                p2 = p2.next
            else:
                val = p1.val
                p1 = p1.next

            p3.next = ListNode(val)
            p3 = p3.next

            print(p1.val if p1 is not None else None)
            print(p2.val if p2 is not None else None)

        return l3.next
        
            

        