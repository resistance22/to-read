from BST import BST, BSTNode


class AVL(BST):
    @staticmethod
    def _fix_avl(node):
        if node.get_balance() > 1:
            right_balance = node.get_right_child().get_balance()
            if right_balance == 1 or right_balance == 0:
                node.left_rotation()
            if right_balance == -1:
                node.get_right_child().right_rotation()
                node.left_rotation()
        if node.get_balance < -1:
            left_balance = node.get_right_child().get_balance()
            if left_balance == -1 or left_balance == 0:
                node.right_rotation()
            if left_balance == 1:
                node.get_left_child().left_rotation()
                node.right_rotation()

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
            AVL._fix_avl(new_node)
        else:
            self.root = BSTNode(data)
