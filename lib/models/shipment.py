import sqlite3

class Shipment:
    def __init__(self, date, status, origin, destination, customer_id):
        self.date = date
        self.status = status
        self.origin = origin
        self.destination = destination
        self.customer_id = customer_id

    def save_to_db(self):
        conn = sqlite3.connect('cargo.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO shipments (date, status, origin, destination, customer_id) VALUES (?, ?, ?, ?, ?)", (self.date, self.status, self.origin, self.destination, self.customer_id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('cargo.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM shipments")
        shipments = cursor.fetchall()
        conn.close()
        return shipments
