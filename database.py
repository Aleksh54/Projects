import sqlite3

dbconnect = sqlite3.connect("dbident.db")
cursor = dbconnect.cursor()

print(type(dbconnect))
print(type(cursor))

new_user = (cursor.lastrowid, "Alexandre", 31)
cursor.execute('INSERT INTO tt_users VALUES (?,?,?)', new_user)
dbconnect.commit()
print('Nouvel utilisateur ajouté"')
dbconnect.close()

