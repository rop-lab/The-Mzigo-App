import sqlite3

def create_tables(conn):
    cursor = conn.cursor()
    
    # Create customers table
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        address TEXT,
                        contact_info TEXT
                    )''')

    # Create packages table
    cursor.execute('''CREATE TABLE IF NOT EXISTS packages (
                        id INTEGER PRIMARY KEY,
                        description TEXT NOT NULL,
                        weight INTEGER,
                        dimensions TEXT,
                        shipment_id INTEGER,
                        FOREIGN KEY (shipment_id) REFERENCES shipments(id)
                    )''')

    # Create shipments table
    cursor.execute('''CREATE TABLE IF NOT EXISTS shipments (
                        id INTEGER PRIMARY KEY,
                        date TEXT,
                        status TEXT,
                        origin TEXT,
                        destination TEXT,
                        customer_id INTEGER,
                        FOREIGN KEY (customer_id) REFERENCES customers(id)
                    )''')

    # Create tracking table
    cursor.execute('''CREATE TABLE IF NOT EXISTS tracking (
                        id INTEGER PRIMARY KEY,
                        status TEXT,
                        location TEXT,
                        shipment_id INTEGER,
                        FOREIGN KEY (shipment_id) REFERENCES shipments(id)
                    )''')

    conn.commit()

def seed_data(conn):
    cursor = conn.cursor()

    # Insert initial data
    cursor.execute("INSERT INTO customers (name, address, contact_info) VALUES (?, ?, ?)", ('Cheruiyot Rop', '123 Main St', 'cheruiyot.rop@gmail.com'))
    cursor.execute("INSERT INTO shipments (date, status, origin, destination, customer_id) VALUES (?, ?, ?, ?, ?)", ('2024-03-20', 'In Transit', 'New York', 'Los Angeles', 1))
    cursor.execute("INSERT INTO packages (description, weight, dimensions, shipment_id) VALUES (?, ?, ?, ?)", ('Box of books', 10, '12x8x6', 1))
    cursor.execute("INSERT INTO tracking (status, location, shipment_id) VALUES (?, ?, ?)", ('In Transit', 'New York', 1))

    conn.commit()

if __name__ == "__main__":
    # Connect to SQLite database
    conn = sqlite3.connect('cargo.db')

    # Create tables
    create_tables(conn)

    # Seed data
    seed_data(conn)

    # Close connection
    conn.close()
