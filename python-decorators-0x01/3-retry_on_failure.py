import time
import sqlite3
import functools


# with_db_connection decorator from the previous task
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


# Retry decorator to retry a function upon failure
def retry_on_failure(retries=3, delay=2):
    """Decorator to retry the function if it raises an exception."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(conn, *args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    # Try running the function
                    return func(conn, *args, **kwargs)
                except Exception as e:
                    # If an error occurs, retry after a delay
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}. Retrying in {delay} seconds...")
                    if attempts >= retries:
                        # If max retries are reached, raise the exception
                        print("Max retries reached. Aborting operation.")
                        raise
                    time.sleep(delay)

        return wrapper

    return decorator


# Function to fetch users from the database with retry logic
@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


# Attempt to fetch users with automatic retry on failure
try:
    users = fetch_users_with_retry()
    print(users)
except Exception as e:
    print(f"Failed to fetch users: {e}")
