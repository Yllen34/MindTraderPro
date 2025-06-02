import sqlite3
import os

# Définir le chemin vers la base de données SQLite
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'journal.db')

def insert_journal_entry(entry):
    """
    Insère une entrée dans la base de données du journal.
    """
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

def get_all_journal_entries():
    """
    Récupère toutes les entrées du journal depuis la base de données.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # permet de convertir les lignes en dictionnaires
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM journal ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]
