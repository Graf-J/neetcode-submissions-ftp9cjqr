class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node_map = {}
        self.dummy_head = Node("<Head>", "<Head>")
        self.dummy_tail = Node("<Tail>", "<Tail>")
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def _add_tail(self, node):
        self.dummy_tail.prev.next = node
        node.prev = self.dummy_tail.prev
        node.next = self.dummy_tail
        self.dummy_tail.prev = node

    def _pop_head(self) -> Node:
        node_to_drop = self.dummy_head.next
        self.dummy_head.next = node_to_drop.next
        self.dummy_head.next.prev = self.dummy_head
        return node_to_drop

    def _move_to_tail(self, node):
        # Remove from current position
        node.prev.next = node.next
        node.next.prev = node.prev
        # Add at Tail
        self._add_tail(node)

    def get(self, key: int) -> int:
        if key not in self.key_node_map:
            return -1

        node = self.key_node_map[key]
        self._move_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.key_node_map:
            node = Node(key, value)
            self._add_tail(node)
            self.key_node_map[key] = node
            if len(self.key_node_map) > self.capacity:
                dropped_head = self._pop_head()
                self.key_node_map.pop(dropped_head.key)
        else:
            node = self.key_node_map[key]
            node.val = value
            self._move_to_tail(node)
















