from avltree import AVLTree

class Menu:
    def __init__(self):
        # self.menu_items = {}
        self.menu_tree = AVLTree()

    def add_item(self, item_name, price, is_drink=False):
        # self.menu_items[item_name] = {'price': price, 'is_drink': is_drink}
        self.menu_tree.add_item(item_name, price, is_drink)
    
    def remove_item(self, item_name):
        return self.menu_tree.remove_item(item_name)
        
    def find_item(self, item_name):
        return self.menu_tree.search(self.menu_tree.root, item_name)
    
    def display_menu(self):
        self.menu_tree.display_menu()
