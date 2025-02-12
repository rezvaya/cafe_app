import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("cafe.db")
cursor = conn.cursor()

# Создание таблиц (уже готово)
cursor.executescript('''
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    price REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    order_date TEXT DEFAULT CURRENT_TIMESTAMP,
    total_price REAL DEFAULT 0,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    menu_id INTEGER,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (menu_id) REFERENCES menu(id)
);
''')

conn.commit()

# 📌 Функции CRUD (нужно реализовать)
def add_client(name, phone, email):
    """Добавляет клиента в базу данных"""
    pass  # TODO: Реализовать добавление клиента

def add_menu_item(item_name, price):
    """Добавляет блюдо в меню"""
    pass  # TODO: Реализовать добавление позиции меню

def create_order(client_id, items):
    """Создает новый заказ"""
    pass  # TODO: Реализовать создание заказа

def list_clients():
    """Выводит список клиентов"""
    pass  # TODO: Реализовать вывод клиентов

def list_menu():
    """Выводит список позиций меню"""
    pass  # TODO: Реализовать вывод меню

def list_orders():
    """Выводит список заказов"""
    pass  # TODO: Реализовать вывод заказов

# 📌 Консольное меню
while True:
    print("\n📋 Меню:")
    print("1. Добавить клиента")
    print("2. Добавить позицию в меню")
    print("3. Создать заказ")
    print("4. Показать клиентов")
    print("5. Показать меню")
    print("6. Показать заказы")
    print("7. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Имя: ")
        phone = input("Телефон: ")
        email = input("Email: ")
        add_client(name, phone, email)

    elif choice == "2":
        item_name = input("Название блюда: ")
        price = float(input("Цена: "))
        add_menu_item(item_name, price)

    elif choice == "3":
        list_clients()
        client_id = int(input("Введите ID клиента: "))
        list_menu()
        items = []
        while True:
            menu_id = int(input("Введите ID блюда (0 для завершения): "))
            if menu_id == 0:
                break
            quantity = int(input("Количество: "))
            items.append((menu_id, quantity))
        create_order(client_id, items)

    elif choice == "4":
        list_clients()

    elif choice == "5":
        list_menu()

    elif choice == "6":
        list_orders()

    elif choice == "7":
        print("👋 Выход из программы.")
        conn.close()
        break

    else:
        print("❌ Неверный выбор, попробуйте снова.")