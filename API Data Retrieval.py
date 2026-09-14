import sqlite3
import requests

# Constants
DB_NAME = "accuknox_assessment.db"
API_URL = "https://openlibrary.org/search.json?q=python&limit=5"

def init_books_db():
    """Initializes the SQLite database and creates the books table."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publication_year INTEGER
        )
    """)
    conn.commit()
    conn.close()

def fetch_and_store_books():
    """Fetches books from REST API and stores them in SQLite."""
    init_books_db()
    
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Request failed: {e}")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Parse JSON and insert records
    docs = data.get("docs", [])
    inserted_count = 0
    
    for doc in docs:
        title = doc.get("title", "Unknown Title")
        # Authors can be a list; grab the first one if available
        authors = doc.get("author_name", ["Unknown Author"])
        author = authors[0] if authors else "Unknown Author"
        
        # Publication year can be first_publish_year
        pub_year = doc.get("first_publish_year", None)

        cursor.execute("""
            INSERT INTO books (title, author, publication_year)
            VALUES (?, ?, ?)
        """, (title, author, pub_year))
        inserted_count += 1

    conn.commit()
    conn.close()
    print(f"Successfully inserted {inserted_count} books into the database.")

def display_books():
    """Retrieves and displays books from the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, title, author, publication_year FROM books")
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Stored Books Database Records ---")
    print(f"{'ID':<4} | {'Title':<40} | {'Author':<25} | {'Year':<6}")
    print("-" * 84)
    for row in rows:
        book_id, title, author, year = row
        # Truncate long strings for clean terminal display
        print(f"{book_id:<4} | {title[:38]:<40} | {author[:23]:<25} | {str(year):<6}")

if __name__ == "__main__":
    fetch_and_store_books()
    display_books()