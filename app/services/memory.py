import sqlite3

class MemoryBank:
    def __init__(self):
        self.conn = sqlite3.connect("memory.db")
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS incidents (user_id TEXT, message TEXT, severity TEXT)"
        )

    def save_incident(self, user_id, message, severity):
        self.conn.execute(
            "INSERT INTO incidents VALUES (?, ?, ?)", (user_id, message, severity)
        )
        self.conn.commit()

    def get_incidents(self, user_id):
        cursor = self.conn.execute(
            "SELECT message, severity FROM incidents WHERE user_id=?", (user_id,)
        )
        return cursor.fetchall()
