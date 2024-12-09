
# Python Generators and MySQL Database Integration

This project demonstrates how to integrate Python with a MySQL database. It includes a script for creating a database, a table, and inserting data from a CSV file into the database. The project also showcases database querying and error handling.

## Features

- **Database Management**: Automatically creates the `ALX_prodev` database if it doesn't exist.
- **Table Management**: Creates a `user_data` table with fields for user ID, name, email, and age.
- **Data Insertion**: Reads data from a CSV file (`user_data.csv`) and inserts it into the `user_data` table.
- **Duplicate Prevention**: Ensures no duplicate emails are added to the table.
- **Error Handling**: Handles common issues such as file not found or database connection errors.

---

## Prerequisites

- Python 3.x
- MySQL Server
- MySQL Connector for Python (`mysql-connector-python`)
- A valid CSV file named `user_data.csv` in the project directory.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shanzaog/alx-backend-python.git
   cd your-repo
   ```

2. Install the required Python packages:
   ```bash
   pip install mysql-connector-python
   ```

3. Set up your MySQL database credentials in `seed.py`:
   ```python
   HOST = "localhost"
   USER = "your_username"
   PASSWORD = "your_password"
   ```

4. Ensure your MySQL server is running.

---

## Usage

1. **Run the script to initialize the database and table**:
   ```bash
   python main.py
   ```

2. **Expected Output**:
   - Database `ALX_prodev` created (if it doesn't already exist).
   - Table `user_data` created (if it doesn't already exist).
   - Data from `user_data.csv` inserted into the table.
   - Sample data from the `user_data` table displayed in the console.

3. **Custom Commands**:
   - Modify `seed.py` to customize table structure or data processing logic.

---

## CSV File Format

Ensure the `user_data.csv` file follows this structure:

```csv
name,email,age
Johnnie Mayer,Ross.Reynolds21@hotmail.com,35
Myrtle Waters,Edmund_Funk@gmail.com,99
Flora Rodriguez,Willie.Bogisich@gmail.com,84
```

---

## File Structure

```
├── seed.py         # Core script for database and data management
├── main.py         # Script to execute the workflow
├── user_data.csv   # Input data file
└── README.md       # Project documentation
```

---

## Troubleshooting

1. **Database Connection Error**:
   - Ensure your MySQL server is running and accessible.
   - Check the credentials in `seed.py`.

2. **CSV File Not Found**:
   - Ensure `user_data.csv` exists in the project directory.
   - Verify the file's format and structure.

3. **Duplicate Email Error**:
   - The script skips inserting records with duplicate emails.

---

## License

This project is open-source and available under the [MIT License](LICENSE).
