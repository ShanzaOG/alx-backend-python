import uuid
import csv
import mysql.connector

# Database connection details (replace with your own)
HOST = "localhost"
USER = "root"
PASSWORD = ""


def connect_db():
    """Connects to the MySQL database server."""
    try:
        connection = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
        return connection
    except mysql.connector.Error as err:
        print("Error connecting to database:", err)
        return None


def create_database(connection):
    """Creates the database if it doesn't exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        connection.commit()
        cursor.close()
        print("Database 'ALX_prodev' created successfully.")
    except mysql.connector.Error as err:
        print("Error creating database:", err)


def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host=HOST, user=USER, password=PASSWORD, database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print("Error connecting to ALX_prodev database:", err)
        return None


def create_table(connection):
    """Creates the user_data table if it doesn't exist."""
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY NOT NULL,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                age INT NOT NULL
            )
            """
        )
        connection.commit()
        cursor.close()
        print("Table 'user_data' created successfully.")
    except mysql.connector.Error as err:
        print("Error creating table:", err)


def insert_data(connection, csv_file_path):
    """Inserts data from a CSV file into the user_data table if it doesn't exist (based on email)."""
    try:
        cursor = connection.cursor()

        # Fetch existing emails to avoid duplicates
        cursor.execute("SELECT email FROM user_data")
        existing_emails = {row[0] for row in cursor.fetchall()}

        # Read data from CSV file
        with open(csv_file_path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["email"] not in existing_emails:
                    user_id = str(uuid.uuid4())
                    sql = (
                        "INSERT INTO user_data (user_id, name, email, age) "
                        "VALUES (%s, %s, %s, %s)"
                    )
                    cursor.execute(
                        sql, (user_id, row["name"], row["email"], int(row["age"]))
                    )
        connection.commit()
        cursor.close()
        print("Data inserted successfully.")
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
    except mysql.connector.Error as err:
        print("Error inserting data:", err)
    except Exception as err:
        print("Unexpected error:", err)
