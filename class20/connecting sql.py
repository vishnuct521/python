# connecting python to mysql
# download pip python sqlconnector
import mysql.connector
conn = mysql.connector.connect(host = "localhost",database = "Workout1",user = "root",password = "vishnuct@123")
cursor = conn.cursor()
print(conn.is_connected())


mysql = "select * from Gym"
# mysql = "select * from Gym where id ='3'"
cursor.execute(mysql)
rows = cursor.fetchall() #this is having the all data
for data in rows:
    print(data)

