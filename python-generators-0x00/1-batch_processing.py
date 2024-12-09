import mysql.connector


def stream_users_in_batches(batch_size):
    """
    Generator function to fetch rows from the user_data table in batches.
    Args:
        batch_size (int): The number of rows to fetch in each batch.
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

        # Fetch and yield data in batches
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break  # Stop when no more data is available
            yield batch

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if connection:
            connection.close()


def batch_processing(batch_size):
    """
    Process each batch of users to filter those over the age of 25.
    Args:
        batch_size (int): The number of rows to process in each batch.
    """
    for batch in stream_users_in_batches(batch_size):
        # Process the batch: filter users older than 25
        filtered_batch = [user for user in batch if user['age'] > 25]

        # Output the filtered batch (or process further as needed)
        for user in filtered_batch:
            print(user)

