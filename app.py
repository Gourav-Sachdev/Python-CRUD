import tornado.ioloop
import json
import requests
import os.path
import tornado.web
import tornado.httpserver
from tornado.gen import Return
import tornado.options
import tornado.httpclient
from tornado import gen

import mysql.connector  #to connect to mysql
from mysql.connector import Error

from tornado.options import define, options
name=""
value={} 

define("port", default=3000, help="run on the given port", type=int)

def getConnection():
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Gourav@sachdev1",
            database="dataweave",
        )
    except Error as e:
        print("Error while connecting to MySQL", e)
    else:
        return connection             
        
def readDBFile():
    connection=getConnection()
    with open('createtable.sql', 'r') as f:
     with connection.cursor() as cursor:
        #print(connection.is_connected()) 
        cursor.execute(f.read(), multi=True)
                     
    
               


               
        




    

class IndexHandler(tornado.web.RequestHandler):
  
    def post(self,operation):  
        print("hello")
        connection=getConnection()
        print(connection)
        cursor = connection.cursor()  

        if operation=="search":
            print("Inside Search loop")
            value=json.loads(self.request.body)
            print(value)
            name=value['item_name']
            cursor.execute("select * from Items where Name= %s",(name,))
            records = cursor.fetchone()
            print(records)
            if cursor.rowcount==1:
                self.write("Given name found")
            else:
                self.write("Given name not found") 
        
        elif operation=="create":
            print("Inside Create loop")
            try:
                value=json.loads(self.request.body)
                print(value)
                item_id =value['item_id']
                name = value['name']
                price= value['price']
                cursor.execute(" insert into Items  values (%s,%s,%s)",(item_id,name, price))
                connection.commit()
                self.write("Item SuccesFully Inserted in the DB")
            except mysql.connector.Error as error:
                self.write("Failed to insert into MySQL table {}".format(error))     
        #tornado.ioloop.IOLoop.current().stop()  

        else:
            print("Inside Update loop")
            try:
                value=json.loads(self.request.body)
                print(value)
                item_name=value['itemname']
                item_id=value['itemid']
                cursor.execute("Update Items set Name = %s where Id = %s",(item_name,item_id))
                #cursor.execute(" insert into Items  values (%s,%s,%s)",(item_id,name, price))
                connection.commit()
                self.write("Item Name SuccesFully updated")
            except mysql.connector.Error as error:
                self.write("Failed to insert into MySQL table {}".format(error))  

""" class AddItem(tornado.web.RequestHandler):

    
    def post(self,user_id):   # Creating a new Item
        print(user_id)
        try:
                value=json.loads(self.request.body)
                print(value)
                item_id =value['item_id']
                name = value['name']
                price= value['price']
                connection=getConnection()
                cursor = connection.cursor()
                cursor.execute(" insert into Items  values (%s,%s,%s)",(item_id,name, price))
                connection.commit()
                self.write("Item SuccesFully Inserted in the DB")
        except mysql.connector.Error as error:
             self.write("Failed to insert into MySQL table {}".format(error))   """


""" class UpdateItem(tornado.web.RequestHandler):

    def post(self):
        try:
            value=json.loads(self.request.body)
            print(value)
            item_name=value['itemname']
            item_id=value['itemid']
            connection=getConnection()
            cursor=connection.cursor()
            cursor.execute("Update Items set Name = %s where Id = %s",(item_name,item_id))
            #cursor.execute(" insert into Items  values (%s,%s,%s)",(item_id,name, price))
            connection.commit()
            self.write("Item Name SuccesFully updated")
        except mysql.connector.Error as error:
             self.write("Failed to insert into MySQL table {}".format(error))   """




            


app = tornado.web.Application(
   # tornado.web.url(r"/", IndexHandler),
   # tornado.web.url(r"/story/([0-9]+)", StoryHandler, "db", name="story")
      handlers=[(r"/(\w+)", IndexHandler)], # ,(r"/(\w+)" ,AddItem),(r"/update" ,UpdateItem)
	  template_path=os.path.join(os.path.dirname(__file__), "templates")
      ,debug=True)

app.listen(3000)
#tornado.ioloop.IOLoop.current().stop()
tornado.ioloop.IOLoop.current().start()
readDBFile()


   







'''
(r'/find', ItemFinder)
class HelloHandler(RequestHandler):
  def get(self):
    self.write({'message': 'hello My name is gourav and I am working on it'})

def make_app():
  urls = [("/", HelloHandler)]
  return Application(urls, debug=True)
  
if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()



   
     async def prepare(self):
        # get_current_user cannot be a coroutine, so set
        # self.current_user in prepare instead.
        user_id = self.get_secure_cookie("blogdemo_user")
        if user_id:
            self.current_user = await self.queryone(
                "SELECT * FROM authors WHERE id = %s", int(user_id)
            )
'''