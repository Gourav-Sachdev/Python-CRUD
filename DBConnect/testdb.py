import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="gourav",
    password="Gourav@sachdev1"
)

mycursor = mydb.cursor()


mycursor.execute("USE dataweave")
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Gourav", "IIIT bangalore")
mycursor.execute(sql, val)



print(mycursor.rowcount, "record inserted.")