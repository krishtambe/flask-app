import pyodbc

SERVER = "203.201.62.108"
DATABASE = "VV2013"
USERNAME = "manmoon"
PASSWORD = "Vml@@dm!n123"

cnxn = pyodbc.connect('DSN={SERVER};Database={DATABASE};UID={USERNAME};PWD={PASSWORD}', autocommit=True)

cursor = cnxn.cursor()
cursor.execute("SELECT * from musers;")

for row in cursor:
    print('row = %r',row)