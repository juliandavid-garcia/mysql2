import os
import datetime
import pymysql
# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')
connection = pymysql.connect(host="localhost",
                            user = username,
                            password = "",
                            db='Chinook')
            
try:
    with connection.cursor() as cursor:
       
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';")
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was succesful
    connection.close()