from BST import BST, BSTNode


class AVL(BST):
    def _fix_avl(self, node):
        temp = node
        while temp is not None:
            if temp.get_balance() > 1:
                if self.is_root(temp):
                    self.root = temp.get_right_child()
                right_balance = temp.get_right_child().get_balance()
                if right_balance == 1 or right_balance == 0:
                    temp.left_rotate()
                if right_balance == -1:
                    temp.get_right_child().right_rotate()
                    temp.left_rotate()
            if temp.get_balance() < -1:
                if self.is_root(temp):
                    self.root = temp.get_left_child()
                left_balance = temp.get_left_child().get_balance()
                if left_balance == -1 or left_balance == 0:
                    temp.right_rotate()
                if left_balance == 1:
                    temp.get_left_child().left_rotate()
                    temp.right_rotate()

            temp = temp.parent

    def insert(self, data):
        if self.root:
            node = self.root
            new_node = BSTNode(data)
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
            BST.update_heights(new_node)
            self._fix_avl(new_node)
        else:
            self.root = BSTNode(data)


if __name__ == '__main__':
    avl = AVL()
    avl.insert(38)
    avl.insert(54)
    avl.insert(55)
    avl.insert(56)
    avl.insert(57)
    avl.insert(58)
    avl.insert(59)
    avl.insert(60)
    avl.display()
