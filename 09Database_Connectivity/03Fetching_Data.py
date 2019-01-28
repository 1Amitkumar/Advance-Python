import MySQLdb as my


db_connect = my.connect(host="localhost",
                        user="root",
                        passwd="",              # put database password
                        db=""                   # put here database name
                        )
print("connection successful")


cursor = db_connect.cursor()                    # cursor is used to make query

query = "select * from table_name"

number_of_rows = cursor.execute(query)
print(number_of_rows)

result = cursor.fetchall()                       # fetchall() method fetch all records
print(result)

db_connect.close()                                  # close connection
