class AdminNode:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.next = None

class AdminLinkedList:
    def __init__(self):
        self.head = None

    def register(self, username, password):
        if self.search(username):
            print("帳號已存在，請使用其他帳號")
            return False
        
        new_admin = AdminNode(username, password)
        new_admin.next = self.head
        self.head = new_admin
        print("管理者註冊成功")
        return True

    def login(self, username, password):
        current = self.head
        while current:
            if current.username == username and current.password == password:
                print("管理者登入成功")
                return True
            current = current.next
        print("帳號或密碼錯誤")
        return False

    def search(self, username):
        current = self.head
        while current:
            if current.username == username:
                return current
            current = current.next
        return None

    def display_admins(self):
        current = self.head
        print("\n--- 管理者列表 ---")
        while current:
            print(f" - {current.username}")
            current = current.next
            
            
            
