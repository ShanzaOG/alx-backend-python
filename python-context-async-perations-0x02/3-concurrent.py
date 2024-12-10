import aiosqlite
import asyncio

# Database setup for demonstration purposes
async def setup_database():
    async with aiosqlite.connect("example_async.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        """)
        await db.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [
            ("Alice", 30),
            ("Bob", 20),
            ("Charlie", 45),
            ("Diana", 50)
        ])
        await db.commit()

# Asynchronous function to fetch all users
async def async_fetch_users():
    async with aiosqlite.connect("example_async.db") as db:
        cursor = await db.execute("SELECT * FROM users")
        results = await cursor.fetchall()
        print("All Users:")
        for row in results:
            print(row)

# Asynchronous function to fetch users older than 40
async def async_fetch_older_users():
    async with aiosqlite.connect("example_async.db") as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > ?", (40,))
        results = await cursor.fetchall()
        print("Users older than 40:")
        for row in results:
            print(row)

# Function to run both queries concurrently
async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

# Main event loop
async def main():
    await setup_database()  # Setup the database
    await fetch_concurrently()  # Run concurrent fetch

# Run the program
asyncio.run(main())
