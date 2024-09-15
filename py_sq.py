# Import SQlite library
import sqlite3

# Connecting to the SQLite database
connection = sqlite3.connect('donations.db')

# Creating a cursor object to interact with the database
cursor = connection.cursor()

# Creating the 'donations' table
cursor.execute('''CREATE TABLE IF NOT EXISTS donations (
                    DonationID INTEGER PRIMARY KEY,
                    DonorName TEXT NOT NULL,
                    Amount REAL NOT NULL,
                    Cause TEXT NOT NULL,
                    Date TEXT NOT NULL)''')

# Inserting a record
cursor.execute("INSERT INTO donations (DonorName, Amount, Cause, Date) VALUES ('Sarath', 500, 'Education Fund', '2024-09-01')")

# Inserting multiple records 
donations_data = [
    ('Bharath', 300, 'Medical Aid', '2024-09-03'),
    ('Lalith', 1000, 'Disaster Relief', '2024-09-07'),
    ('Lekha', 150, 'Animal Welfare', '2024-09-10')
]

# Inserting each record into the table which are existing in database
for donation in donations_data:
    cursor.execute("INSERT INTO donations (DonorName, Amount, Cause, Date) VALUES (?, ?, ?, ?)", donation)

# Querying the database
cursor.execute("SELECT * FROM donations")
rows = cursor.fetchall()

# Querying a table that doesn't exist
try:
    cursor.execute("SELECT * FROM non_existing_table")  # This table doesn't exist
except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")    

# Printing the records from the donations table
print("\nRecords in the 'donations' table:")
for row in rows:
    print(row)

# Commiting the changes to the database
connection.commit()

# Closing the connection
connection.close()