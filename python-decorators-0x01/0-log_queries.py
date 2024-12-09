import sqlite3
import functools

# Decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log the query being executed
        query = kwargs.get('query') or args[0]  # Assuming query is passed as a keyword or positional argument
        print(f"Executing SQL query: {query}")
        return func(*args, **kwargs)  # Call the original function
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
query = "SELECT * FROM user_data"
users = fetch_all_users(query=query)
print(users)
