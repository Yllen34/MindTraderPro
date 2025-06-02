import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), '../database/journal.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_entry(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO journal (date, paire, type, lot, entry, sl, tp, rr, gain, note, tag, audio_path)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('date', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        data['paire'],
        data['type'],
        data['lot'],
        data['entry'],
        data['sl'],
        data['tp'],
        data['rr'],
        data['gain'],
        data['note'],
        data.get('tag'),
        data.get('audio_path')
    ))

    conn.commit()
    conn.close()

def get_all_entries():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM journal').fetchall()
    conn.close()
    return [dict(e) for e in entries]

def update_entry(entry_id, data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE journal
        SET date = ?, paire = ?, type = ?, lot = ?, entry = ?, sl = ?, tp = ?, rr = ?, gain = ?, note = ?, tag = ?, audio_path = ?
        WHERE id = ?
    ''', (
        data.get('date', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        data['paire'],
        data['type'],
        data['lot'],
        data['entry'],
        data['sl'],
        data['tp'],
        data['rr'],
        data['gain'],
        data['note'],
        data.get('tag'),
        data.get('audio_path'),
        entry_id
    ))

    conn.commit()
    conn.close()

def delete_entry(entry_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM journal WHERE id = ?', (entry_id,))
    conn.commit()
    conn.close()
