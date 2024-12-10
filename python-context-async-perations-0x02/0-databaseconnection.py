import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        # Open the database connection and return the cursor
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        # Commit changes and close the connection
        if self.connection:
            if exc_type is None:
                self.connection.commit()  # Commit if no exception occurred
            self.connection.close()

# Using the context manager
db_name = 'example.db'

# Setup for demonstration purposes (create table and insert data)
with sqlite3.connect(db_name) as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie')")
    conn.commit()

# Use the DatabaseConnection context manager
with DatabaseConnection(db_name) as cursor:
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print("Query Results:")
    for row in results:
        print(row)
