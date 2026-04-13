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
        # Dummy head helps avoid null checks for the front of the list
        self.head = Node(0, 0)
        self.tail = self.head

    def _move_to_tail(self, node):
        if node is self.tail:
            return
        
        # 1. Snip the node out of its current position
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        # 2. Attach it after the current tail
        node.prev = self.tail
        node.next = None
        self.tail.next = node
        
        # 3. Update the tail pointer
        self.tail = node

    def get(self, key: int) -> int:
        if key not in self.key_node_map:
            return -1
        
        node = self.key_node_map[key]
        self._move_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.val = value  # Update value
            self._move_to_tail(node)
        else:
            new_node = Node(key, value)
            self.key_node_map[key] = new_node
            
            # Link to tail
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
            # Check capacity
            if len(self.key_node_map) > self.capacity:
                # Remove the Least Recently Used (the one after dummy head)
                lru = self.head.next
                self.key_node_map.pop(lru.key)
                
                self.head.next = lru.next
                if lru.next:
                    lru.next.prev = self.head
                else:
                    # If we just deleted the only node, tail must point to head
                    self.tail = self.head