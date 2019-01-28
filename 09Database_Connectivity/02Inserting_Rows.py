import MySQLdb as my


db_connect = my.connect(host="localhost",
                        user="root",
                        passwd="",              # put database password
                        db=""                   # put here database name
                        )
print("connection successful")


cursor = db_connect.cursor()                    # cursor is used to make query

query = "insert into table_name VALUES( )"

number_of_rows = cursor.execute(query)
print(number_of_rows)
db_connect.commit()                             # commit() method to save changes to the database

db_connect.close()                              # close connection
