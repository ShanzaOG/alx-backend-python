import mysql.connector


def stream_users():
    """
    Generator function to fetch rows one by one from the user_data table.
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

        # Execute query to fetch all rows from the user_data table
        cursor.execute("SELECT * FROM user_data")

        # Use a generator to yield rows one by one
        for row in cursor:
            yield row

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if connection:
            connection.close()
