class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummy_left = Node()
        self.dummy_right = Node()
        self.dummy_left.next = self.dummy_right
        self.dummy_right.prev = self.dummy_left

    def remove_node(self, node: Node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left

    def append_node(self, node: Node):
        left, right = self.dummy_right.prev, self.dummy_right
        left.next = node
        node.prev = left
        right.prev = node
        node.next = right

    def popleft_node(self) -> Node:
        left, node, right = self.dummy_left, self.dummy_left.next, self.dummy_left.next.next
        left.next = right
        right.prev = left
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove_node(node)
        self.append_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.append_node(node)
            return

        node = Node(key, value)
        self.append_node(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            node = self.popleft_node()
            self.cache.pop(node.key)
















        
