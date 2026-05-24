class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # ---------------- SUM ----------------
    def recursive_sum(self):
        return self._sum(self.head)

    def _sum(self, node):
        if node is None:
            return 0
        return node.data + self._sum(node.next)

    # ---------------- SEARCH ----------------
    def recursive_search(self, target):
        return self._search(self.head, target)

    def _search(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        return self._search(node.next, target)

    # ---------------- REVERSE ----------------
    def recursive_reverse(self):
        self.head = self._reverse(None, self.head)

    def _reverse(self, prev, current):
        if current is None:
            return prev

        next_node = current.next
        current.next = prev
        return self._reverse(current, next_node)