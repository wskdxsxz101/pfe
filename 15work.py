import sqlite3

conn = sqlite3.connect('study.sqlite')
cur = conn.execute('DROP TABLE IF EXISTS Study')
cur.execute('''
CREATE TABLE Study(email TXET,count INTIEGER)''')

fhand = open('mbox-short.txt')
for line in fhand:
    if not line.startswith('From'): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Study WHERE email = ?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Study(email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Study SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()
