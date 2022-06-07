import sqlite3

con = sqlite3.connect('domashka_3.db')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS category
               (id integer primary key, name text unique, parent integer, descr )''')

cur.execute("INSERT INTO category VALUES ('1','Vasya','15','very'), ('2','Petya','20','not very')")

cur.execute('''CREATE TABLE IF NOT EXISTS product
               (id integer primary key, name text, descr text, category integer not null )''')

cur.execute("INSERT INTO product VALUES ('1','Mashynka','Krasnaya','28'), ('2','Samolyotik','Siniy','32')")

for row in cur.execute('SELECT * FROM category WHERE id'):
        print(row)

sql = "SELECT * FROM product WHERE name=?"
cur.execute(sql, [("Mashynka")])
print(cur.fetchone())

con.commit()

con.close()