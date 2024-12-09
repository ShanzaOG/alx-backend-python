import sqlite3
import functools


# with_db_connection from the previous task
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


# Transactional decorator to handle commits and rollbacks
def transactional(func):
    """Decorator to ensure the function runs within a transaction."""

    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            # Start the transaction
            result = func(conn, *args, **kwargs)
            # Commit the transaction if no error occurs
            conn.commit()
            return result
        except Exception as e:
            # Rollback the transaction if an error occurs
            conn.rollback()
            print(f"Transaction failed: {e}")
            raise

    return wrapper


# Example function that updates a user's email
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))


# Update user's email with automatic transaction handling
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
