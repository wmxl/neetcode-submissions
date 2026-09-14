class ListNode:
    def __init__(self, key="", val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"({self.prev.val if self.prev else None}-{self.val}-{self.next.val if self.next else None})"
    
    def prt(self, limit=30):
        parts = []
        p = self
        seen = set()
        while p and len(parts) < limit:
            if id(p) in seen:
                parts.append(f"↺{p.key}")   # 环回到这个节点
                break
            seen.add(id(p))
            parts.append(f"{p.key}:{p.val}")
            p = p.next
        return "-".join(parts)

class LRUCache:
    
    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        d = self.d
        if key in d:
            node = d[key]
            self.move_to_tail(node)
            return node.val
        return -1        

    def put(self, key: int, value: int) -> None:
        d = self.d
        if key in d:
            # update and move to tail
            node = d[key]
            node.val = value
            self.move_to_tail(node)
        else:
            # print(self.head.prt() if self.head else None)
            # new a ListNode, add to tail 
            if self.tail:
                self.tail.next = ListNode(key, value, None, self.tail)
                self.tail = self.tail.next
            else:
                self.tail = ListNode(key, value, None, self.tail)
            # add ListNode as d's value
            d[key] = self.tail
            # if first item, set head
            if len(d) == 1:
                self.head = self.tail
            # check capacity, remove head if need
            if len(d) > self.capacity:
                del d[self.head.key]
                self.head = self.head.next
                self.head.prev = None
           
    def move_to_tail(self, node):
        if self.tail == node:
            return 
        if node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            # node must be head 
            if len(self.d) > 1:
                self.head = self.head.next
                self.head.prev = None

        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
                