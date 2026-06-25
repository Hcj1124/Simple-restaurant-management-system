import sys
from menu import Menu
from order import Order
from admin import AdminLinkedList
from avltree import AVLTree

admin_list = AdminLinkedList()
admin_list.register("admin", "admin")

def admin_avl_menu(menu):
    while True:
        print("\n--- AVLTree菜單管理 ---")
        print("1. 新增菜單項目")
        print("2. 刪除菜單項目")
        print("3. 搜尋菜單項目")
        print("4. 顯示菜單項目")
        print("5. 返回管理者面板")
        
        choice = input("請選擇功能: ")
        if choice == '1':
            item_name = input("請輸入菜單項目名稱: ")
            try:
                price = int(input("請輸入價格: "))
                is_drink = input("是否為飲料?(y/n): ").lower() == 'y'
                menu.add_item(item_name, price, is_drink)
                print(f"已將 {item_name} 新增至菜單，價格為 ${price:.0f}")
            except ValueError:
                print("輸入無效，請重新輸入")
        elif choice == '2':
            item_name = input("請輸入要刪除的菜單項目名稱: ")
            node = menu.find_item(item_name)
            if node:
                menu.remove_item(item_name)
                print(f"已刪除項目: {item_name}")
            else:
                print("菜單中沒有該項目")
        elif choice == '3':
            item_name = input("請輸入要搜尋的菜單項目名稱: ")
            node = menu.find_item(item_name)
            if node:
                print(f"{node.key}: ${node.price}")
            else:
                print("菜單中沒有該項目")
        elif choice == '4':
            menu.display_menu()
        elif choice == '5':
            break
        else:
            print("選項無效，請重新選擇")

def admin_mode(menu, order):
    while True:
        print("\n--- 管理者模式 ---")
        print("1. 管理者登入")
        print("2. 管理者註冊")
        print("3. 返回主選單")
        admin_choice = input("請選擇功能: ")
    
        if admin_choice == '1':
            username = input("請輸入管理者帳號: ")
            password = input("請輸入管理者密碼: ")
            if admin_list.login(username, password):
                admin_panel(menu, order)
        elif admin_choice == '2':
            username = input("請輸入新管理者帳號: ")
            password = input("請輸入新管理者密碼: ")
            if admin_list.register(username, password):
                print("\n--- 管理者登入 ---")
                username = input("請輸入管理者帳號: ")
                password = input("請輸入管理者密碼: ")
                if admin_list.login(username, password):
                    admin_panel(menu, order)
        elif admin_choice == '3':
            print("返回主選單")
            break
        else:
            print("選項無效，請重新選擇")

def admin_panel(menu, order):
    while True:
        print("\n--- 管理者面板 ---")
        print("1. 檢視所有訂單")
        print("2. 顯示管理者帳號")
        print("3. AVLTree菜單管理")
        print("4. 登出")
        
        choice = input("請選擇功能: ")
        if choice == '1':
            print("\n--- 所有訂單 ---")
            if not Order.all_orders:
                print("無訂單資料")
            for receipt in Order.all_orders:
                print(f"\n訂單編號: {receipt['id']}")
                for item in receipt['items']:
                    ice_level_str = item['ice_level'][1] if item['ice_level'] else ""
                    print(f"{item['item_name']}{ice_level_str}: {item['quantity']} x ${item['price']:.0f}")
                print(f"總金額: ${receipt['total']:.0f}")
        elif choice == '2':
            admin_list.display_admins()
        elif choice == '3':
            admin_avl_menu(menu)
        elif choice == '4':
            print("已登出")
            break
        else:
            print("選項無效，請重新選擇")


def customer_mode(menu, order):
    print("\n--- 顧客模式 ---")
    menu.display_menu()
    while True:
        item_name = input("請輸入欲點餐的項目 (按 Enter 完成點餐, 輸入 delete 可移除最後一項, 輸入 back 回到主選單): ")
        
        if item_name == "":
            if order.head:
                order.display_order()
                order.save_receipt()
                print("感謝您的點餐")
            else:
                print("您尚未點餐")
            break

        if item_name.lower() == 'back':
            print("返回主選單")
            break

        if item_name.lower() == 'delete':
            order.remove_last_item()
            continue
        
        node = menu.find_item(item_name)
        if node:
            try:
                quantity = int(input(f"請輸入 {item_name} 的數量: "))
                if quantity < 1:
                    raise ValueError("數量不能為負數或零")
                order.add_item(item_name, quantity)
            except ValueError:
                print("請輸入有效的數量。")
        else:
            print("菜單中沒有這個項目，請重新輸入")

def main():
    try:
        menu = Menu()
        menu.add_item("Salad", 80)
        menu.add_item("Hotdog", 120)
        menu.add_item("Burger", 150)
        menu.add_item("Pizza", 200)
        menu.add_item("Coffee", 25, is_drink=True)
        menu.add_item("Tea", 25, is_drink=True)

        order = Order(menu)

        while True:
            print("\n--- 主選單 ---")
            print("1. 顧客模式")
            print("2. 管理者模式")
            print("3. 結束程式")
            choice = input("請選擇模式: ")

            if choice == '1':
                customer_mode(menu, order)
            elif choice == '2':
                admin_mode(menu, order)
            elif choice == '3':
                print("程式已結束")
                sys.exit(0)
            else:
                print("輸入無效，請重新輸入")
    except Exception as e:
        print(f"程式執行時發生錯誤：{e}")

main()
