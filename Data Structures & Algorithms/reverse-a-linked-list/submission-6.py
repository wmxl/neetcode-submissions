# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, cur):
            if cur == None:
                return prev
            
            next_cur = cur.next
            cur.next = prev
            return reverse(cur, next_cur)
            
        return reverse(None, head)


