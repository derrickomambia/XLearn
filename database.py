import sqlite3
import time

def get_db_connection():
    conn = sqlite3.connect('education.db')
    return conn

def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    
    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS units (
        unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
        unit_name TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS questions (
        question_id INTEGER PRIMARY KEY AUTOINCREMENT,
        unit_id INTEGER,
        question_text TEXT,
        options TEXT,
        correct_answer TEXT,
        FOREIGN KEY (unit_id) REFERENCES units(unit_id))''')
    
    # Remove test_sessions and test_answers tables since they’re no longer needed
    c.execute("DROP TABLE IF EXISTS test_sessions")
    c.execute("DROP TABLE IF EXISTS test_answers")
    
    # Insert "Electromagnetism" as the unit
    c.execute("INSERT OR IGNORE INTO units (unit_id, unit_name) VALUES (1, 'Electromagnetism')")
    
    # Sample questions for Electromagnetism (placeholders; replace with your full list)
    c.execute("INSERT OR IGNORE INTO questions (unit_id, question_text, options, correct_answer) VALUES (1, 'Explain the meaning of Electromagnetism.', '', 'Electromagnetism is the study of the interactions between electric and magnetic fields.')")
    c.execute("INSERT OR IGNORE INTO questions (unit_id, question_text, options, correct_answer) VALUES (1, 'Explain the meaning of Electromagnetic force.', '', 'Electromagnetic force is the force between charged particles due to their electric and magnetic fields.')")
    
    conn.commit()
    conn.close()

def add_question(unit_id, question_text, options, correct_answer):
    # Ensure options is a string (default to '' if None or not a string)
    if options is None or not isinstance(options, str):
        options = ''
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO questions (unit_id, question_text, options, correct_answer) VALUES (?, ?, ?, ?)", 
              (unit_id, question_text, options, correct_answer))
    conn.commit()
    conn.close()
    return c.lastrowid

def get_user(username, password):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    return user

def add_user(username, password):
    conn = get_db_connection()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

def get_units():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM units")
    units = c.fetchall()
    conn.close()
    return units

def get_questions(unit_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM questions WHERE unit_id = ?", (unit_id,))
    questions = c.fetchall()
    conn.close()
    return questions