# The-Mzigo-App

# customer.py
This Python code provides a simple Customer Management System using SQLite as the database backend.

The application allows users to create, read, update and delete customers in the system. It also includes functionalities for adding new products. 
## Installation and Usage:
1. Clone this repository to your local machine
2. Make sure you have Python installed on your  system (version 3.6 or above)
3. Open terminal/command prompt, navigate to the cloned folder

## Usage
1. Instantiate the Customer class with necessary parameters such as name, address, and contact information.
2. Use the save_to_db() method to save the customer data to the SQLite database.
3. Retrieve all customers from the database using the get_all() class method.
4. Retrieve a specific customer by ID using the get_by_id(customer_id) class method.


Customer Management System
This Python code provides a simple Customer Management System using SQLite as the database backend.

Requirements
Python 3.x
SQLite3
Installation
Clone or download the repository.
Ensure you have Python and SQLite installed on your system.
Run the code using any Python IDE or execute it via command line.
Usage
Instantiate the Customer class with necessary parameters such as name, address, and contact information.
Use the save_to_db() method to save the customer data to the SQLite database.
Retrieve all customers from the database using the get_all() class method.
Retrieve a specific customer by ID using the get_by_id(customer_id) class method.
Example
python
Copy code
from customer_management import Customer

# Create a new customer
customer1 = Customer("John Doe", "123 Main St", "john@example.com")
customer1.save_to_db()

# Retrieve all customers
all_customers = Customer.get_all()
print("All Customers:", all_customers)

# Retrieve a specific customer by ID
customer_id = 1
specific_customer = Customer.get_by_id(customer_id)
print("Specific Customer:", specific_customer)

## Database
The code uses a SQLite database named cargo.db to store customer information. The database schema consists of a single table named customers with the following columns:

id: Integer (Primary Key, Auto Increment)
name: Text
address: Text
contact_info: Text
## Note
Uncomment the delete() method if you want to implement customer deletion functionality.
Make sure to handle exceptions appropriately for database connections and queries.