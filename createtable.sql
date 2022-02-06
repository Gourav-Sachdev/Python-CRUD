/* use dataweave; */
drop table if exists Items;
create table Items(Id int(10) NOT NULL Primary key,Name varchar(50) NOT NULL,Price int(20) NOT NULL);
insert into Items values(1,"Soap",100),(2,"Comb",50),(3,"Belt",170),(4,"Wallet",84);
commit;



/*
        print("Brigade")    

        """ if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("use dataweave;")
           
            print("You're connected to database: ")"""

except Error as e:
    print("Error while connecting to MySQL", e)

"""cursor.execute("drop table if exists Items")
createTableQuery=""" #create table Items(Id int(10) NOT NULL Primary key,
                        #                Name varchar(50) NOT NULL,
                         #               Price int(20) NOT NULL)"""

""" """ # insertTableQuery=""" insert into Items values(%s,%s,%s)"""
# val = [(2,"Soap",23),
#     (3,"Comb",53),
#     (4,"Shampoo",83),
#     (5,"Phone",983)
#     ]

# select_Query=""" Select * from Items  """
 cursor.execute(createTableQuery)
connection.commit()    
cursor.executemany(insertTableQuery,val) 
connection.commit()

cursor.execute(select_Query)
# get all records
records = cursor.fetchall()

print("Total number of rows in table: ", cursor.rowcount)

print("\nPrinting each row")
for row in records:
    print("Id = ", row[0], )
    print("Name = ", row[1])
    print("Price  = ", row[2],"\n") 


    """ response=requests.post('http://localhost:3000/create')
    api_url = "https://jsonplaceholder.typicode.com/todos"
    todo = {"userId": 1, "title": "Buy milk", "completed": False}
    response = requests.post(api_url, json=todo)
    response.json()  
    """
    
    */