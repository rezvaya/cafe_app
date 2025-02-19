import sqlite3
from abc import ABC, abstractmethod

class Datsbase(ABC):
    @abstractmethod
    def execute(self, query, params=()):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod    
    def fetchone(self, query, params=()):
        pass

    @abstractmethod    
    def fetchall(self, query, params=()):
        pass


class SQLiteDB(Datsbase):
    def __init__(self, db_path = "cafe1.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self):
        self.cursor.executescript('''
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
        self.conn.commit()

    def execute(self, query, params=()):
        self.cursor.execute(query, params=())

    def commit(self):
        self.conn.commit()
 
    def fetchone(self, query, params=()):
        self.cursor.execute(query, params=())
        return self.cursor.fetchone()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params=())
        return self.cursor.fetchall()

# MenuManager
# ClientManager
# OrderManager 