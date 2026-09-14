# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 1 Keep the first half of the array unchanged, and reverse the order of the second half.
        # 2 Split into 2 list(one is original sort, anther is reversed sort)
        # 3 Alternatively take item from 2 list and form a new one

        # if head is None:
        #     return

        fast = head
        slow = head 
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        reverse = slow.next 
        slow.next = None

        l, m = None, reverse
        while m:
            r = m.next
            m.next = l
            l = m
            m = r
        reverse = l
        
        p3 = new_list = ListNode()
        p1 = head
        p2 = reverse
        while p1:
            p3.next = p1
            p3 = p3.next
            p1 = p1.next

            if p2:
                p3.next = p2
                p3 = p3.next
                p2 = p2.next
            
        
            