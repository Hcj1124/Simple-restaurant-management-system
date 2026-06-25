class AVLNode:
    def __init__(self, key, price, is_drink):
        self.key = key
        self.price = price
        self.is_drink = is_drink
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def insert(self, node, key, price, is_drink):
        if not node:
            return AVLNode(key, price, is_drink)

        if key < node.key:
            node.left = self.insert(node.left, key, price, is_drink)
        elif key > node.key:
            node.right = self.insert(node.right, key, price, is_drink)
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node
    
    def remove(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self.remove(node.left, key)
        elif key > node.key:
            node.right = self.remove(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.get_min_value_node(node.right)
            node.key = temp.key
            node.price = temp.price
            node.is_drink = temp.is_drink
            node.right = self.remove(node.right, temp.key)

        if not node:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
    
    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, node, key):
        if not node or node.key == key:
            return node

        if key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"{node.key}: ${node.price}")
            self.inorder(node.right)

    def add_item(self, key, price, is_drink=False):
        self.root = self.insert(self.root, key, price, is_drink)
        
    def remove_item(self, key):
        self.root = self.remove(self.root, key)
    
    def display_menu(self):
        print("\n-------- 菜單 --------")
        self.inorder(self.root)
