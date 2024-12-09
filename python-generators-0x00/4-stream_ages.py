import mysql.connector

def stream_user_ages():
    """
    Generator function to yield user ages one by one from the database.
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

        # SQL query to fetch user data
        cursor.execute("SELECT age FROM user_data")

        # Yield user ages one by one
        for row in cursor:
            yield row['age']  # Yield the age of each user

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if connection:
            connection.close()


def calculate_average_age():
    """
    Function to calculate the average age of users using the stream_user_ages generator.
    """
    total_age = 0
    user_count = 0

    # Use the generator to fetch user ages and calculate the sum and count
    for age in stream_user_ages():
        total_age += age
        user_count += 1

    # Calculate the average age
    if user_count > 0:
        average_age = total_age / user_count
        print(f"Average age of users: {average_age}")
    else:
        print("No user data available.")

# Example usage:
if __name__ == "__main__":
    calculate_average_age()
