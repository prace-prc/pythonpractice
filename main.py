import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port='5432',
    dbname='library',
    user='postgres',
    password='1234'
)

cursor = conn.cursor()
# cursor.execute('SELECT * FROM Books;')

cursor.execute('''
CREATE TABLE test_table (
id SERIAL PRIMARY KEY,
name VARCHAR(50))
''')

conn.commit()

cursor.close()
conn.close()