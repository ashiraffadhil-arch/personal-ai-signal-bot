import sqlite3

DATABASE_NAME = "signals.db"

def connect(): return sqlite3.connect(DATABASE_NAME)

def initialize_database(): with connect() as conn: conn.execute(""" CREATE TABLE IF NOT EXISTS analyses ( id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT NOT NULL, description TEXT, probability REAL, confidence TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ) """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            analysis_id INTEGER NOT NULL,
            actual_result TEXT NOT NULL,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (analysis_id) REFERENCES analyses(id)
        )
    """)


def save_analysis(category, description, probability, confidence): with connect() as conn: cursor = conn.execute(""" INSERT INTO analyses (category, description, probability, confidence) VALUES (?, ?, ?, ?) """, (category, description, probability, confidence))

    return cursor.lastrowid


def save_result(analysis_id, actual_result): with connect() as conn: conn.execute(""" INSERT INTO results (analysis_id, actual_result) VALUES (?, ?) """, (analysis_id, actual_result))

def get_analysis_history(limit=20): with connect() as conn: cursor = conn.execute(""" SELECT * FROM analyses ORDER BY id DESC LIMIT ? """, (limit,))

    return cursor.fetchall()


if name == "main": initialize_database() print("Database initialized successfully.")
