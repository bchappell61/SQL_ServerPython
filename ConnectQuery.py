# pip install pyodbc
import pyodbc


# A variable for the sql query
# Hard coded id number 
IDNumber = '101'

# Connection info for Database
conn_str = (
    r'Driver={SQL Server};'
    r'Server=<ServerName>;'
    r'Database=<your Database Name>;'
    r'Trusted_Connection=yes;'
    )

'''
# replace Trusted_Connection with user & pwd if not Single Sign on
r'UID=<your userName>;'
r'PWD=<your password>;'
'''

# Query table for attributes The ? is a placeholder for a variable
sql = """SELECT * 
         FROM <TableName>
         WHERE <TableName>.<ID_Field> = ?; """

cnxn = pyodbc.connect(conn_str)

cursor = cnxn.cursor()

# IDNumber is the variable for the placeholder in sql query
cursor.execute(sql,(IDNumber))

# Fetchone brings back the matching record for that ID number
result = cursor.fetchone()

print(result)

'''
PYODBC Docs
https://github.com/mkleehammer/pyodbc/wiki

Select Basics

All SQL statements are executed using the Cursor execute() function. 
If the statement returns rows, such as a select statement, 
you can retrieve them using the Cursor fetch functions - fetchone(), fetchall(), fetchmany(). 
If there are no rows, fetchone() will return None, 
whereas fetchall() and fetchmany() will both return empty lists.
For more than one row returned:

cursor.execute("select user_id, user_name from users")

result = cursor.fetchall()

for row in result:
    print(row.user_id, row.user_name)

    print(row[0], row[1]  # Option, instead of fieldnames

# example (u'101', u'John Doe')
'''