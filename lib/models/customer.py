import sqlite3

class Customer:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info

    def save_to_db(self):
        conn = sqlite3.connect('cargo.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, address, contact_info) VALUES (?, ?, ?)", (self.name, self.address, self.contact_info))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('cargo.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
        conn.close()
        return customers
    
    @classmethod
    def delete_by_name(cls, name):
        conn = sqlite3.connect('cargo.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers WHERE name=?", (name,))
        conn.commit()
        conn.close()
