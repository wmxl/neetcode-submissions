# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head
        # Invariant: sentinel..lasts_before_reverse_head is finished
        # lasts_before_reverse_head.next is the first unprocessed node
        lasts_before_reverse_head = sentinel

        prob = head
        while True:
            before_reverse_head = prob
            # Walk k nodes, stop early if the list runs out. 
            cnt = k
            while cnt > 0 and prob:
                cnt -= 1 
                prob = prob.next
            # Fewer than k left, the invariant already holds.
            if cnt > 0:
                return sentinel.next
            # prob is now the first node of next group(may be None, means no next group) 

            # Reverse this group
            cur = before_reverse_head
            # prev set to next group's head, so after reverse it, this group 's old head(new tail) automatically connect to new group 
            prev = prob
            while cur != prob:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next 
            # After loop, prev(old tail) became this group's new head
            
            # Last group's old head(new tail) connect to this group's new head
            lasts_before_reverse_head.next = prev
            lasts_before_reverse_head = before_reverse_head



        