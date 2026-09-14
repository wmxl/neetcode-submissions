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

        p = head
        while p:
            if d.get(p):
                curNode = d[p]
            else:
                curNode = Node(p.val)
                d[p] = curNode

            if p.random and d.get(p.random):
                randomNode = d.get(p.random)
            elif p.random:
                randomNode = Node(p.random.val)
                d[p.random] = randomNode
            else:
                randomNode = None

            curNode.random = randomNode

            p1.next = curNode
            p1 = p1.next
            p = p.next

        p1.next = None
        
        return head1.next
        
