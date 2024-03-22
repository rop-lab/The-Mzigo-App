from models.customer import Customer
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


# def delete_customer():
#     id_= input ("costomer_id")
#     if customer:= customer.get_all(id_):
#         customer.delete()
#         print (f'Customer with ID={id_} has been deleted.')
#     else:
#         print ('Customer not found.')
def delete_customer():
    customer_id = input("Enter the ID of the customer you want to delete: ")

    # Retrieve the customer by ID
    customer = Customer.get_by_id(customer_id)

    if customer:
        print("Customer found:")
        print(f"ID: {customer.id}, Name: {customer.name}, Address: {customer.address}, Contact Info: {customer.contact_info}")
        
        # Ask for confirmation before deletion
        confirmation = input("Are you sure you want to delete this customer? (yes/no): ").lower()
        if confirmation == "yes":
            # Delete the customer
            customer.delete()
            print("Customer deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Customer not found.")


# def add_to_database():


if __name__ == "__main__":
    print("This script contains helper functions for displaying data from the database.")
