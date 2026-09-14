# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 探针最开始指向head，本轮反转的从当前探针开始，反转前记录before_reverse_head = 探针, 
# 弄一个头哨兵， 哨兵.next = head
# last_before_reverse_head = 哨兵

# 然后跑探针，如果不够k-1直接结束，够k-1且不是None, last_before_reverse_head.next = 这个k-1，一直到k停下（可以是null)，

# 然后以探针为prev，从 before_reverse_head 开始反转这组链表，反转到最后一个后，last_before_reverse_head 更新为 before_reverse_head，
# 然后进行下一轮跑探针...

# 最后return哨兵.next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head
        lasts_before_reverse_head = sentinel

        prob = head
        while True:
            before_reverse_head = prob
            # run the prob, if not enough to k, end
            cnt = k
            while cnt > 0 and prob:
                cnt -= 1 
                prob = prob.next
            # after loop prob is next group's head

            if cnt > 0:
                return sentinel.next

            # reverse this group
            cur = before_reverse_head
            # prev set to next group's head, so after reverse it, this group 's old head(new tail) automatically connect to new group 
            prev = prob
            while cur != prob:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next 
            # after loop, prev(old tail) became this group's new head
            # last group's old head(new tail) connect to this group's new head
            lasts_before_reverse_head.next = prev
            lasts_before_reverse_head = before_reverse_head



        