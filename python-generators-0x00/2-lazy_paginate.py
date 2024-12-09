import mysql.connector


def paginate_users(page_size, offset):
    """
    Fetches a specific page of users from the database.
    Args:
        page_size (int): The number of rows to fetch per page.
        offset (int): The offset for the SQL query to fetch the next page.
    """
    connection = None
    try:
        # Database connection details (replace with your own)
        HOST = "localhost"
        USER = "root"
        PASSWORD = ""
        DATABASE = "ALX_prodev"

        # Connect to the database
        connection = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
        cursor = connection.cursor(dictionary=True)

        # SQL query to fetch users with pagination
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))

        # Fetch the result
        return cursor.fetchall()

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if connection:
            connection.close()


def lazy_pagination(page_size):
    """
    Generator function to lazily fetch pages of users with the given page_size.
    Each page will only be fetched when needed.
    Args:
        page_size (int): The number of rows to fetch per page.
    """
    offset = 0
    while True:
        # Fetch the next page of users
        page = paginate_users(page_size, offset)

        # If no data is returned, stop the iteration
        if not page:
            break

        # Yield the current page of users
        yield page

        # Increment the offset for the next page
        offset += page_size


# Example usage:
if __name__ == "__main__":
    page_size = 5  # Set page size
    for page in lazy_paginate(page_size):
        print(page)  # Print each page of users
