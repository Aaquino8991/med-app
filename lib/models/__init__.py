import sqlite3

CONN = sqlite3.connect('records.db')
CURSOR = CONN.cursor()