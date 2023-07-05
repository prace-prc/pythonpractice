import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port='5432',
    dbname='library',
    user='postgres',
    password='1234'
)

cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE test_table (
# id SERIAL PRIMARY KEY,
# name VARCHAR(50))
# ''')
# conn.commit()

# cursor.execute("INSERT INTO test_table (name) VALUES (%s)", ("Test name",))
# conn.commit()

cursor.execute("update test_table set name = 'Change' where id = 1")
conn.commit()

cursor.execute('SELECT * FROM test_table;')
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
