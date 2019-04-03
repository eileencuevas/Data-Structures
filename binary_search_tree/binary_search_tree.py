class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = BinarySearchTree(value)
        if value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value > target:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        elif self.value < target:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        else:
            return True

    def get_max(self):
        current_max = 0
        current_node = self
        while current_node is not None:
            current_max = max(current_node.value, current_max)
            current_node = current_node.right
        return current_max

    def for_each(self, cb):
        # performs a traversal of every node in the tree, executing the passed-in
        # callback function on each tree node value
        # while self.left is not None and self.right is not None:
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)
