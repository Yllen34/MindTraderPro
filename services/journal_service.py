import sqlite3
import os

# Détermine le chemin vers la base (à adapter si Render PostgreSQL ensuite)
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'journal.db')

def insert_journal_entry(entry):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO journal (
            pair, entry, sl, tp, result,
            risked_amount, strategy, emotion,
            respected_plan, commentaire
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        entry['pair'],
        entry['entry'],
        entry['sl'],
        entry['tp'],
        entry['result'],
        entry['risked_amount'],
        entry['strategy'],
        entry['emotion'],
        entry['respected_plan'],
        entry.get('commentaire', "")
    ))

    conn.commit()
    conn.close()
