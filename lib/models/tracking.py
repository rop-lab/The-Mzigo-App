import sqlite3

class Tracking:
    def __init__(self, status, location, shipment_id):
        self.status = status
        self.location = location
        self.shipment_id = shipment_id

    def save_to_db(self):
        conn = sqlite3.connect('cargo.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tracking (status, location, shipment_id) VALUES (?, ?, ?)", (self.status, self.location, self.shipment_id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('cargo.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tracking")
        tracking = cursor.fetchall()
        conn.close()
        return tracking
