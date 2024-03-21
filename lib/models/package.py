import sqlite3

class Package:
    def __init__(self, description, weight, dimensions, shipment_id):
        self.description = description
        self.weight = weight
        self.dimensions = dimensions
        self.shipment_id = shipment_id

    def save_to_db(self):
        conn = sqlite3.connect('cargo.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO packages (description, weight, dimensions, shipment_id) VALUES (?, ?, ?, ?)", (self.description, self.weight, self.dimensions, self.shipment_id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('cargo.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM packages")
        packages = cursor.fetchall()
        conn.close()
        return packages
