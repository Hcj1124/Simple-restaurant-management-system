class Node:
    def __init__(self, item_name, quantity, price, ice_level=None):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.ice_level = ice_level
        self.next = None

class Order:
    all_orders = []
    
    def __init__(self, menu):
        self.head = None
        self.menu = menu

    def add_item(self, item_name, quantity):
        node = self.menu.find_item(item_name)
        if not node:
            print("菜單中沒有這個項目")
            return

        price = node.price
        is_drink = node.is_drink

        if is_drink:
            ice_level = self.get_ice_level(item_name)
        else:
            ice_level = None

        current = self.head
        while current:
            if current.item_name == item_name and current.ice_level == ice_level:
                current.quantity += quantity
                return
            current = current.next

        new_node = Node(item_name, quantity, price, ice_level)
        new_node.next = self.head
        self.head = new_node
        
    def get_ice_level(self, item_name):
        print("請選擇冰量:")
        print("1. 正常")
        print("2. 少冰")
        print("3. 去冰")
        choice = input("請輸入選擇的數字: ")
        ice_levels = {1: ("正常", ""), 2: ("少冰", "*"), 3: ("去冰", "^")}

        try:
            selected_ice_level = ice_levels[int(choice)]
            return selected_ice_level
        except KeyError:
            print("選擇無效，使用預設值 '正常'")
            return ("正常", "")

    def remove_last_item(self):
        if self.head:
            removed_item = self.head
            self.head = self.head.next
            print(f"已移除最後一項: {removed_item.item_name} x {removed_item.quantity}")
        else:
            print("訂單為空，無法移除項目。")

    def calculate_total(self):
        total = 0
        current = self.head
        while current:
            total += current.quantity * current.price
            current = current.next
        return total

    def display_order(self):
        print("-------- 收據 --------")
        current = self.head
        if not current:
            print("訂單為空")
            return

        while current:
            ice_level_str = current.ice_level[1] if current.ice_level else ""
            print(f"{current.item_name}{ice_level_str}: {current.quantity} x ${current.price:.0f}")
            current = current.next

        print(f"總金額: ${self.calculate_total():.0f}")
        
    def save_receipt(self):
        if not self.head:
            print("沒有訂單可儲存")
            return

        order_summary = {
            "id": len(Order.all_orders) + 1,
            "items": [],
            "total": self.calculate_total()
        }
        
        current = self.head
        while current:
            order_summary["items"].append({
                "item_name": current.item_name,
                "quantity": current.quantity,
                "price": current.price,
                "ice_level": current.ice_level
            })
            current = current.next

        Order.all_orders.append(order_summary)
        print(f"訂單已儲存 (訂單編號: {order_summary['id']})")
        self.head = None

        
        
