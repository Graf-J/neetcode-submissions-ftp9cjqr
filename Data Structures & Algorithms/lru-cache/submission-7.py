class Node:
    def __init__(self, key="", val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def insert_tail(self, node):
        self.dummy_tail.prev.next = node
        node.prev = self.dummy_tail.prev
        node.next = self.dummy_tail
        self.dummy_tail.prev = node

    def move_to_tail(self, node):
        # Remove from current position
        node.prev.next = node.next
        node.next.prev = node.prev
        # Insert Tail
        self.insert_tail(node)

    def pop_head(self):
        pop_node = self.dummy_head.next
        self.dummy_head.next = self.dummy_head.next.next
        self.dummy_head.next.prev = self.dummy_head
        return pop_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.move_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.move_to_tail(self.cache[key])
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert_tail(node)
            if len(self.cache) > self.capacity:
                pop_node = self.pop_head()
                self.cache.pop(pop_node.key)











