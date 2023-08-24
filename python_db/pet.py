import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Password@123",
    database="animal"
)

cursor=db.cursor()

query="""insert into pets(age,gender,breed,location,price)values(17,"female","breed1","kochi",2000"""

cursor.execute(query) 
db.commit()