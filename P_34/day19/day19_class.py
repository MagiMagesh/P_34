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

    def insertions(self,table_name):
        query = f'select column_name from information_schema.columns where table_name = "{table_name}"'
        cursor = self.db.cursor() # we need to create a cursor
        cursor.execute(query)
        column = cursor.fetchall()
        # input = {i[0]:input(f'Enter the data for {i[0]}') for i in column}
        for i in column:
            v = input(f'Enter the data for {i[0]}: ') # you need to structure this as value
            print(f"{i[0]}: ",v)


database = connect_db()
# database.selection('student1')
# print(10*'-')
# database.selection('student')
database.insertions('student')