import sqlite3

conn = sqlite3.connect("tennis.db")
c = conn.cursor()
c.execute("DELETE FROM matches")
conn.commit()
conn.close()

