"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        head1 = Node(0)
        p1 = head1

        def copy(p):
            if p is None:
                return None
            if p not in d:
                d[p] = Node(p.val)
            return d[p]
        
        p = head
        while p:
            curNode = copy(p)
            curNode.random = copy(p.random)
            
            p1.next = curNode
            p1 = p1.next
            p = p.next

        return head1.next
        
