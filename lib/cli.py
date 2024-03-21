from helpers import display_customers, display_packages, display_shipments, display_tracking
from models.customer import Customer
from models.package import Package
from models.shipment import Shipment
from models.tracking import Tracking

def main():
    while True:
        print("\nWelcome to the Cargo Management System!")
        print("1. Customers")
        print("2. Packages")
        print("3. Shipments")
        print("4. Tracking")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer_menu()
        elif choice == '2':
            package_menu()
        elif choice == '3':
            shipment_menu()
        elif choice == '4':
            tracking_menu()
        elif choice == '5':
            print("Thank you for using the Cargo Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. Add Customer")
        print("2. Display Customers")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            contact_info = input("Enter customer contact info: ")
            customer = Customer(name, address, contact_info)
            customer.save_to_db()
            print("Customer added successfully!")
        elif choice == '2':
            print("\nList of Customers:")
            display_customers()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

def package_menu():
    while True:
        print("\nPackage Menu:")
        print("1. Add Package")
        print("2. Display Packages")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter package description: ")
            weight = input("Enter package weight: ")
            dimensions = input("Enter package dimensions: ")
            shipment_id = input("Enter shipment ID: ")
            package = Package(description, weight, dimensions, shipment_id)
            package.save_to_db()
            print("Package added successfully!")
        elif choice == '2':
            print("\nList of Packages:")
            display_packages()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

def shipment_menu():
    while True:
        print("\nShipment Menu:")
        print("1. Add Shipment")
        print("2. Display Shipments")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter shipment date: ")
            status = input("Enter shipment status: ")
            origin = input("Enter shipment origin: ")
            destination = input("Enter shipment destination: ")
            customer_id = input("Enter customer ID: ")
            shipment = Shipment(date, status, origin, destination, customer_id)
            shipment.save_to_db()
            print("Shipment added successfully!")
        elif choice == '2':
            print("\nList of Shipments:")
            display_shipments()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

def tracking_menu():
    while True:
        print("\nTracking Menu:")
        print("1. Add Tracking Information")
        print("2. Display Tracking Information")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            status = input("Enter tracking status: ")
            location = input("Enter tracking location: ")
            shipment_id = input("Enter shipment ID: ")
            tracking = Tracking(status, location, shipment_id)
            tracking.save_to_db()
            print("Tracking information added successfully!")
        elif choice == '2':
            print("\nList of Tracking Information:")
            display_tracking()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

if __name__ == "__main__":
    main()
