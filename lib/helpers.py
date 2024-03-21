import sqlite3

def display_customers():
    conn = sqlite3.connect('cargo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    conn.close()

    if not customers:
        print("No customers found.")
    else:
        for customer in customers:
            print(f"ID: {customer[0]}, Name: {customer[1]}, Address: {customer[2]}, Contact Info: {customer[3]}")

def display_packages():
    conn = sqlite3.connect('cargo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM packages")
    packages = cursor.fetchall()
    conn.close()

    if not packages:
        print("No packages found.")
    else:
        for package in packages:
            print(f"ID: {package[0]}, Description: {package[1]}, Weight: {package[2]}, Dimensions: {package[3]}, Shipment ID: {package[4]}")

def display_shipments():
    conn = sqlite3.connect('cargo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shipments")
    shipments = cursor.fetchall()
    conn.close()

    if not shipments:
        print("No shipments found.")
    else:
        for shipment in shipments:
            print(f"ID: {shipment[0]}, Date: {shipment[1]}, Status: {shipment[2]}, Origin: {shipment[3]}, Destination: {shipment[4]}, Customer ID: {shipment[5]}")

def display_tracking():
    conn = sqlite3.connect('cargo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tracking")
    tracking = cursor.fetchall()
    conn.close()

    if not tracking:
        print("No tracking information found.")
    else:
        for track in tracking:
            print(f"ID: {track[0]}, Status: {track[1]}, Location: {track[2]}, Shipment ID: {track[3]}")

if __name__ == "__main__":
    print("This script contains helper functions for displaying data from the database.")
