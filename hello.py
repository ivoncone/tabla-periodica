import sqlite3
import random

conn = sqlite3.connect('elements.db')
c = conn.cursor()

c.execute("SELECT symbol FROM elements")
elements = c.fetchall()
for symbol in elements:
	if symbol < 21:
		print(symbol)



c.execute("SELECT atomic_number FROM elements")
elements = c.fetchall()

for atomic_number in elements:
	print(sorted(atomic_number))

c.execute("SELECT * FROM elements")
elements = c.fetchall()


