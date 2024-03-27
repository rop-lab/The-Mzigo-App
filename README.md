# The-Mzigo-App

## Customer Management System
This Python code provides a simple Customer Management System using SQLite as the database backend.

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

# package.py
This is a Python implementation of a simple package management system using SQLite3 for data storage. The system allows users to create packages with descriptions, weights, dimensions, and associate them with shipment IDs. It provides functionalities to save packages to a database and retrieve all packages from the database.

# Usage
Class: Package
The Package class represents a package with the following attributes:

- description: Description of the package.
- weight: Weight of the package.
- dimensions: Dimensions of the package.
- shipment_id: ID of the shipment associated with the package.

## Methods:
__init__(self, description, weight, dimensions, shipment_id): Initializes a new instance of the Package class with the provided attributes.

save_to_db(self): Saves the package details to the SQLite database named cargo.db.

get_all(cls): Retrieves all packages stored in the database.

# Database Schema
The SQLite database schema consists of a single table named packages with the following columns:

- id: Primary key, auto-incremented integer.
- description: Text field to store the description of the package.
- weight: Real number field to store the weight of the package.
- dimensions: Text field to store the dimensions of the package.
- shipment_id: Integer field to store the ID of the shipment associated with the package.

## shipment.py
# Shipment Management System

This Python code provides functionality for managing shipments using SQLite database.

## Features

- Create new shipments
- Retrieve all shipments

## Prerequisites

- Python 3.x
- SQLite

## Installation

1. Clone the repository:

2. Navigate to the project directory:


3. Ensure you have SQLite installed on your system.

## Usage

1. Import the `Shipment` class into your Python script:

```python
from shipment import Shipment

- Create a new shipment:
shipment = Shipment(date='2024-03-27', status='In transit', origin='City A', destination='City B', customer_id=123)
shipment.save_to_db()

Retrieve all shipments:
shipments = Shipment.get_all()
print(shipments)
