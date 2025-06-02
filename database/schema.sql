CREATE TABLE IF NOT EXISTS journal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pair TEXT NOT NULL,
    entry REAL NOT NULL,
    sl REAL NOT NULL,
    tp REAL NOT NULL,
    result TEXT NOT NULL, -- 'win', 'loss', 'be'
    risked_amount REAL NOT NULL,
    strategy TEXT NOT NULL,
    emotion TEXT NOT NULL,
    respected_plan BOOLEAN NOT NULL,
    commentaire TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
