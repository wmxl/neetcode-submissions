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
        while p1 and p2:
            if p1.val > p2.val:
                p3.next = p2
                p2 = p2.next
            else:
                p3.next = p1
                p1 = p1.next
            p3 = p3.next
        p3.next = p2 if p2 is not None else p1
        
        return l3.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None

        while n > 1:
            for i in range(n // 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[n - 1 - i])
            n = (n + 1) // 2
         
        return lists[0]

