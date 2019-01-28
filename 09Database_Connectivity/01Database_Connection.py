# 1 Create a connection.
# 2 Create a cursor object.
# 3 Close the connection.


import MySQLdb as my


db_connect = my.connect(host="localhost",       # 1
                        user="root",
                        passwd="",              # put database password
                        db=""                   # put here database name
                        )
print(db_connect)
print("connection successful")


cursor = db_connect.cursor()                    # 2 cursor is used to make query

db_connect.close()                              # 3 close connection
