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
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        d = self.d
        if key in d:
            node = d[key]
            self.remove(node)
            self.add_to_tail(node)
            return node.val
        return -1        

    def put(self, key: int, value: int) -> None:
        d = self.d
        if key in d:
            # update and move to tail
            node = d[key]
            node.val = value
            self.remove(node)
            self.add_to_tail(node)
        else:
            # new a ListNode, add to tail 
            node = ListNode(key, value)
            self.add_to_tail(node)
            # add ListNode as d's value
            d[key] = node
            # check capacity, remove head if need
            if len(d) > self.capacity:
                del d[self.head.next.key]
                self.remove(self.head.next)
           
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_tail(self, node):
        prev_node = self.tail.prev
        
        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node
    
                