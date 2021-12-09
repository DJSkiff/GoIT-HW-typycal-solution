import sqlite3


with open('query_1.sql') as f:
    sql = f.read()

with sqlite3.connect('education.db') as conn:
    cursor = conn.cursor()
    cursor.execute(sql)
    print(cursor.fetchall())
