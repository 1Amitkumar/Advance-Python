import MySQLdb as my


try:
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

    db_connect.close()                               # close connection


# DB error handling
# to check please enter invalid entries eg:wrong database name, password, table etc.

except my.DataError as e:
    print("Data_Error")
    print(e)

except my.InternalError as e:
    print("Internal_Error")
    print(e)

except my.IntegrityError as e:
    print("Integrity_Error")
    print(e)

except my.OperationalError as e:
    print("Operational_Error")
    print(e)

except my.NotSupportedError as e:
    print("Not_Supported_Error")
    print(e)

except my.ProgrammingError as e:
    print("Programming_Error")
    print(e)

except:
    print("Unknown error occurred")
