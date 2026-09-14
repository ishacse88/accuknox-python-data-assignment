import csv
import os
import sqlite3

DB_NAME = "accuknox_assessment.db"
CSV_FILE_PATH = "users_sample.csv"

def create_sample_csv():
    """Helper function to create a dummy CSV file for demonstration."""
    data = [
        ["name", "email"],
        ["John Doe", "john.doe@example.com"],
        ["Jane Smith", "jane.smith@example.com"],
        ["Alex Johnson", "alex.j@example.com"]
    ]
    with open(CSV_FILE_PATH, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def import_csv_to_sqlite():
    """Reads user info from CSV and batch inserts into SQLite database."""
    # Create sample CSV file if it doesn't exist
    if not os.path.exists(CSV_FILE_PATH):
        create_sample_csv()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

    # Read and insert CSV data
    inserted_count = 0
    duplicate_count = 0

    try:
        with open(CSV_FILE_PATH, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get("name")
                email = row.get("email")
                
                try:
                    cursor.execute("""
                        INSERT INTO users (name, email)
                        VALUES (?, ?)
                    """, (name, email))
                    inserted_count += 1
                except sqlite3.IntegrityError:
                    # Handle duplicate emails gracefully
                    duplicate_count += 1

        conn.commit()
        print(f"CSV Import Complete. Inserted: {inserted_count}, Skipped (Duplicates): {duplicate_count}")

    except Exception as e:
        print(f"An error occurred during CSV import: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    import_csv_to_sqlite()