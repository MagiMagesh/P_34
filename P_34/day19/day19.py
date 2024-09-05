import mysql.connector

db = mysql.connector.connect(
    # host = 'localhost',
    host = '127.0.0.1',
    user = 'root',
    password = 'magesh1234',
    port = '3306',
    database = 'p34'

)

print(db)

# query = 'use p34' # not highly reccommended
# cursor = db.cursor() # we need to create a cursor
# cursor.execute(query)
# print(cursor)


# query = 'select * from student'
# cursor = db.cursor() # we need to create a cursor
# cursor.execute(query)
# print(cursor.fetchall()) # [(1,2,3,4),(11,12,13,14)]


query = "insert into student1 values (5,'M','mages@123.sadf',1000,'no');"
cursor = db.cursor() # we need to create a cursor
cursor.execute(query)

db.commit() # data will not be inserted

print(cursor)