import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None

    def __enter__(self):
        # Open the database connection and create a cursor
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self

    def execute(self):
        # Execute the query with parameters and return results
        if self.params:
            self.cursor.execute(self.query, self.params)
        else:
            self.cursor.execute(self.query)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_value, traceback):
        # Commit changes and close the connection
        if self.connection:
            if exc_type is None:
                self.connection.commit()  # Commit if no exception occurred
            self.connection.close()

# Setup for demonstration purposes (create table and insert data)
db_name = 'example.db'
with sqlite3.connect(db_name) as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    conn.execute("INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 20), ('Charlie', 35)")
    conn.commit()

# Use the ExecuteQuery context manager
query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery(db_name, query, params) as context_manager:
    results = context_manager.execute()
    print("Query Results:")
    for row in results:
        print(row)
