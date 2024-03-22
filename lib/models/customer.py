import sqlite3

class Customer:
    def __init__(self, name, address, contact_info, id=None):
        self.id = id
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
    
    # def delete(self):
    #     conn = sqlite3.connect('cargo.db')
    #     cursor = conn.cursor()
    #     cursor.execute("DELETE FROM customers WHERE id=?")
    #     conn.commit()
    #     conn.close()
    
    @classmethod
    def get_by_id(cls, customer_id):
        conn = sqlite3.connect('cargo.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE id = ?", (customer_id,))
        customer_data = cursor.fetchone()
        conn.close()

        if customer_data:
            return cls(*customer_data)
        else:
            return None