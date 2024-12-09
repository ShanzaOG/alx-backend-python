import time
import sqlite3
import functools

# Cache to store query results
query_cache = {}


# with_db_connection decorator from previous tasks
def with_db_connection(func):
    """Decorator to automatically handle opening and closing database connections."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Open a new database connection
        conn = sqlite3.connect('users.db')

        try:
            # Pass the connection to the original function
            return func(conn, *args, **kwargs)
        finally:
            # Ensure the connection is closed after the function executes
            conn.close()

    return wrapper


# Cache query decorator
def cache_query(func):
    """Decorator to cache SQL query results based on the query string."""

    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        # Check if the query result is already cached
        if query in query_cache:
            print("Returning cached result for query:", query)
            return query_cache[query]

        # If not cached, call the function to execute the query
        result = func(conn, query, *args, **kwargs)

        # Store the result in the cache
        query_cache[query] = result

        return result

    return wrapper


# Function to fetch users from the database with caching
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print("First call:", users)

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print("Second call (cached):", users_again)
