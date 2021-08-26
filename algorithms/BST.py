from random import randint


class BSTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.height = 0
        self.size = 1
        self.data = data

    def hasLeftChild(self):
        return bool(self.left)

    def hasRightChild(self):
        return bool(self.right)

    def setLeftChild(self, node):
        self.left = node

    def setRightChild(self, node):
        self.right = node

    def getRightChild(self):
        return self.right

    def getLefChild(self):
        return self.left

    def getData(self):
        return self.data

    def __str__(self):
        return str(self.data)

    def updateSize(self):
        self.size = self.size + 1

    def getChildernMaxHeight(self):
        if self.hasRightChild() and self.hasLeftChild():
            return max(self.left.height, self.right.height)
        if self.hasLeftChild() and not self.hasRightChild():
            return self.left.height
        if self.hasRightChild() and not self.hasLeftChild():
            return self.right.height
        if not (self.hasLeftChild() or self.hasRightChild()):
            return -1

    def updateHeight(self):
        self.height = self.getChildernMaxHeight() + 1

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

    def updateHeights(self, path):
        while(path):
            node = path.pop()
            node.updateHeight()

    def getHeight(self):
        return self.root.height

    def insert(self, data):
        if self.root:
            node = self.root
            path = []
            while True:
                path.append(node)
                node.updateSize()
                if data >= node.getData():
                    if node.hasRightChild():
                        node = node.getRightChild()
                    else:
                        node.setRightChild(BSTNode(data))
                        break
                else:
                    if node.hasLeftChild():
                        node = node.getLefChild()
                    else:
                        node.setLeftChild(BSTNode(data))
                        break
            self.updateHeights(path)
        else:
            self.root = BSTNode(data)

    def __str__(self):
        if(self.root.hasLeftChild()):
            pass

    def getSize(self):
        return self.root.size


if __name__ == '__main__':
    bst = BST()
    for _ in range(20):
        bst.insert(randint(0, 150))
    bst.display()
