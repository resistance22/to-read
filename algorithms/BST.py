from random import randint


class BSTNode:
    def __init__(self, data):
        self.left: 'BSTNode' or None = None
        self.right: 'BSTNode' or None = None
        self.parent: 'BSTNode' or None = None
        self.height: int = 0
        self.size: int = 1
        self.data: int or float = data

    def has_left_child(self) -> bool:
        return bool(self.left)

    def set_parent(self, node: 'BSTNode' or None):
        self.parent = node

    def has_right_child(self):
        return bool(self.right)

    def set_left_child(self, node: 'BSTNode'):
        self.left = node
        if not (node is None):
            node.parent = self

    def set_right_child(self, node: 'BSTNode'):
        self.right = node
        if not (node is None):
            node.parent = self

    def get_right_child(self) -> 'BSTNode':
        return self.right

    def get_left_child(self) -> 'BSTNode':
        return self.left

    def get_data(self):
        return self.data

    def __str__(self):
        return str(self.data)

    def update_size(self):
        self.size = self.size + 1

    def get_children_max_height(self) -> int:
        if self.has_right_child() and self.has_left_child():
            return max(self.left.height, self.right.height)
        if self.has_left_child() and not self.has_right_child():
            return self.left.height
        if self.has_right_child() and not self.has_left_child():
            return self.right.height
        if not (self.has_left_child() or self.has_right_child()):
            return -1

    def update_height(self):
        self.height = self.get_children_max_height() + 1

    def get_balance(self) -> int:
        if self.has_right_child() and self.has_left_child():
            return self.right.height - self.left.height
        if self.has_left_child() and not self.has_right_child():
            return -1 - self.left.height
        if self.has_right_child() and not self.has_left_child():
            return self.right.height + 1
        if not (self.has_left_child() or self.has_right_child()):
            return 0

    def get_parent(self) -> 'BSTNode':
        return self.parent

    def right_rotate(self):
        y = self.get_left_child()
        parent = self.parent
        beta = y.get_right_child()
        y.set_right_child(self)
        self.set_left_child(beta)
        if parent is not None and parent.get_left_child() is self:
            parent.set_left_child(y)
        elif parent is not None and parent.get_right_child() is self:
            parent.set_right_child(y)
        elif parent is None:
            y.set_parent(None)

        self.update_height()
        y.update_height()

    def left_rotate(self):
        x = self.get_right_child()
        parent = self.parent
        beta = x.get_left_child()
        x.set_left_child(self)
        self.set_right_child(beta)
        if parent is not None and parent.get_left_child() is self:
            parent.set_left_child(x)
        elif parent is not None and parent.get_right_child() is self:
            parent.set_right_child(x)
        elif parent is None:
            x.set_parent(None)

        self.update_height()
        x.update_height()

    def get_height(self) -> int:
        return self.height

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % str(self.data) + '|' + \
                str(self.height) + '|' + str(self.size)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % str(self.data) + '|' + \
                str(self.height) + '|' + str(self.size)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % str(self.data) + '|' + \
                str(self.height) + '|' + str(self.size)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % str(self.data) + '|' + \
            str(self.height) + '|' + str(self.size)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BST:
    def __init__(self):
        self.root = None

    def display(self):
        self.root.display()

    def is_root(self, node):
        return self.root == node

    def lca(self, first, second):
        node = self.root
        while True:
            if node.data > first and node.data > second:
                node = node.get_left_child()
            elif node.data < first and node.data < second:
                node = node.get_right_child()
            else:
                return node

    @staticmethod
    def update_heights(node: 'BSTNode'):
        temp = node
        while temp.parent:
            temp.update_height()
            temp = temp.parent
        else:
            temp.update_height()

    def get_height(self):
        return self.root.height

    def _insert(self, data: int):
        new_node = BSTNode(data)
        if self.root:
            node = self.root
            while True:
                node.update_size()
                if data >= node.get_data():
                    if node.has_right_child():
                        node = node.get_right_child()
                    else:
                        node.set_right_child(new_node)
                        new_node.set_parent(node)
                        break
                else:
                    if node.has_left_child():
                        node = node.get_left_child()
                    else:
                        node.set_left_child(new_node)
                        new_node.set_parent(node)
                        break
        else:
            self.root = BSTNode(data)

        return new_node

    def insert(self, data: int):
        new_node = self._insert(data)
        BST.update_heights(new_node)

    def __str__(self):
        if self.root.has_left_child():
            pass

    def get_size(self):
        return self.root.size


if __name__ == '__main__':
    bst = BST()
    bst.insert(38)
    bst.insert(39)
    bst.insert(40)
    bst.insert(50)
    bst.insert(51)
    bst.insert(52)
    bst.insert(53)
    bst.insert(54)

    bst.display()
