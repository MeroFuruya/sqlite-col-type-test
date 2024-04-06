import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

# NOTE: we create a column that has LENGTH **1**
c.execute('''CREATE TABLE test
          (testVarchar VARCHAR(1))
          ''')
conn.commit()

# NOTE: we insert a string that is longer than the column definition
c.execute("INSERT INTO test VALUES ('aaaa')")
conn.commit()

res = c.execute("SELECT * FROM test")

# NOTE: we can see that the string is inserted successfully

for row in res:
    print(row)

conn.close()

print('If you read this, it means SQLite column definitions are an illusion and im gonna stick my finger up my ass because of it.')