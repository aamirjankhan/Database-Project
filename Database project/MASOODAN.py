import pyodbc
driver= '{SQL Server Native Client 11.0}'

con = pyodbc.connect(
    Trusted_Connection='Yes',
    Driver='{ODBC Driver 11 for SQL Server}',
    Server='DESKTOP-KKLDKIP\SQLEXPRESS',
    Database='Test'
)

cur = con.cursor()
#cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts1 (email text, count int)''')

# cur.execute('''
# CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts1 WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts1 (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts1 SET count = count + 1 WHERE email = ?',
                    (email,))
    con.commit()


sqlstr = 'SELECT email, count FROM Counts1 ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()