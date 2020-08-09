import pyodbc
driver= '{SQL Server Native Client 11.0}'

con = pyodbc.connect(
    Trusted_Connection='Yes',
    Driver='{ODBC Driver 11 for SQL Server}',
    Server='DESKTOP-KKLDKIP\SQLEXPRESS',
    Database='Test'
)

cur = con.cursor()
cur.execute("CREATE DATABASE mydatabase")

