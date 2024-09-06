# 2. regular expression

# 1. database project
# 2. interview questions
# 3. doubt clarifications 



import mysql.connector


class connect_db:
    def __init__(self) :
        self.db = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'magesh1234',
            port = '3306',
            database = 'p34'
        )

    def selection(self,table_name):
        query = f'select * from  {table_name}'
        cursor = self.db.cursor() # we need to create a cursor
        cursor.execute(query)
        print(cursor.fetchall())

database = connect_db()
# database.selection('student1')
# print(10*'-')
# database.selection('student')
# database.insertions('student')
database.insertions('student2')

