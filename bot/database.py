import sqlite3
import logging


class DatabaseManager:
    def __init__(self, db_path="entries.db"):
        try:
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            self._create_table()
        except sqlite3.Error as e:
            logging.error(f"Veritabanı bağlantı hatası: {e}")

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id TEXT PRIMARY KEY,
                title TEXT,
                link TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def entry_exists(self, entry_id):
        self.cursor.execute("SELECT 1 FROM entries WHERE id = ?", (entry_id,))
        return self.cursor.fetchone() is not None

    def add_entry(self, entry_id, title, link):
        try:
            self.cursor.execute(
                "INSERT OR IGNORE INTO entries (id, title, link) VALUES (?, ?, ?)", 
                (entry_id, title, link)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_recent_entries(self, limit=5):
        self.cursor.execute("""
            SELECT id, title, link 
            FROM entries 
            ORDER BY rowid DESC
            LIMIT ?
        """, (limit,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
