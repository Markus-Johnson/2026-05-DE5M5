import pyodbc
import time

# Give SQL Server a few seconds to start up
time.sleep(10)

# ── Connect to SQL Server ───────────────────────────────────────
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=sql_server,1433;"
    "UID=sa;"
    "PWD=YourPassword123!;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()

# ── Create the database ─────────────────────────────────────────
cursor.execute("IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'LibraryDB') CREATE DATABASE LibraryDB")
cursor.execute("USE LibraryDB")

# ── Create the tables ───────────────────────────────────────────
cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Customers' AND xtype='U')
    CREATE TABLE Customers (
        Customer_ID INT PRIMARY KEY,
        Customer_Name VARCHAR(255) NOT NULL
    )
""")

cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Books' AND xtype='U')
    CREATE TABLE Books (
        Id INT PRIMARY KEY,
        Books VARCHAR(255) NOT NULL,
        Book_Checkout DATE,
        Book_Returned DATE,
        Days_Allowed_To_Borrow VARCHAR(50),
        Customer_ID INT NOT NULL,
        FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID)
    )
""")

# ── Insert some data ────────────────────────────────────────────
cursor.execute("INSERT INTO Customers (Customer_ID, Customer_Name) VALUES (1, 'Jane Doe')")
cursor.execute("INSERT INTO Customers (Customer_ID, Customer_Name) VALUES (2, 'John Smith')")

cursor.execute("""
    INSERT INTO Books (Id, Books, Book_Checkout, Book_Returned, Days_Allowed_To_Borrow, Customer_ID)
    VALUES (1, 'Catcher in the Rye', '2023-02-20', '2023-02-25', '2 weeks', 1)
""")

conn.commit()

# ── Verify data was written ─────────────────────────────────────
cursor.execute("SELECT * FROM Customers")
print("\nCustomers table:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Books")
print("\nBooks table:")
for row in cursor.fetchall():
    print(row)

print("\nData written successfully!")
conn.close()