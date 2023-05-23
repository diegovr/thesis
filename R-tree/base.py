import math

class RTree:

    def __init__(self, capacity):
        self.capacity = capacity
        self.root = None

    def insert(self, point):
        if self.root is None:
            self.root = Node(point)
        else:
            self._insert(self.root, point)

    def _insert(self, node, point):
        if node.is_full():
            new_node = Node()
            new_node.children.append(node)
            self._split(node, new_node)
            self._insert(new_node, point)
        else:
            node.children.append(point)
            node._rebalance()

    def _split(self, old_node, new_node):
        mid = math.floor(len(old_node.children) / 2)
        for i in range(mid):
            new_node.children.append(old_node.children[i])
        old_node.children = old_node.children[mid:]

    def query(self, query_box):
        if self.root is None:
            return []
        else:
            return self._query(self.root, query_box)

    def _query(self, node, query_box):
        results = []
        if node.bounding_box.intersects(query_box):
            for child in node.children:
                if child.bounding_box.intersects(query_box):
                    results.append(child)
                if child.is_leaf():
                    results.append(child)
        return results


class Node:

    def __init__(self, point=None):
        self.point = point
        self.children = []
        self.bounding_box = None

    def is_full(self):
        return len(self.children) == self.capacity

    def is_leaf(self):
        return len(self.children) == 0

    def _rebalance(self):
        if self.is_full():
            mid = math.floor(len(self.children) / 2)
            self.children.sort(key=lambda child: child.bounding_box.area())
            self.children[mid], self.children[-1] = self.children[-1], self.children[mid]

    def bounding_box(self):
        if self.bounding_box is None:
            self.bounding_box = self.point.bounding_box()
        return self.bounding_box

