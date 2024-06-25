import sqlite3


def init_db():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            A INTEGER,
            B INTEGER
        )
    """
    )
    # Check if the table is empty
    c.execute("SELECT * FROM data")
    if c.fetchone() is None:
        # Insert initial data
        c.executemany(
            "INSERT INTO data (A, B) VALUES (?, ?)", [(10, 100), (20, 200), (30, 300)]
        )
    conn.commit()
    conn.close()


def query_db(query, args=(), one=False):
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv


def insert_or_update_db(rows):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    # Insert or replace data
    cur.executemany(
        "REPLACE INTO data (id, A, B) VALUES (?, ?, ?)",
        [(row.get("id"), row.get("A"), row.get("B")) for row in rows],
    )
    conn.commit()
    conn.close()
