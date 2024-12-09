import sqlite3
import functools
from datetime import datetime


# Decorator to log SQL queries with the timestamp
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Get the SQL query from the arguments (either keyword or positional argument)
        query = kwargs.get('query') or args[0]

        # Log the timestamp and the SQL query
        print(f"[{timestamp}] Executing SQL query: {query}")

        # Call the original function
        return func(*args, **kwargs)

    return wrapper


# Function to fetch all users from the database
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# Example usage: Fetch users while logging the query
query = "SELECT * FROM users"
users = fetch_all_users(query=query)
print(users)
