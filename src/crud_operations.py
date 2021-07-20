"""
@Author: Rikesh Chhetri
@Date: 2021-07-19
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-19 10:03:30
@Title : Program Aim perform CRUD operations and storing data in mysql database. 
"""
from mysql.connector import cursor
import os
import mysql.connector as connector
from LoggerHandler import logger
from dotenv import load_dotenv
load_dotenv()

class CrudOperations:

   def __init__(self):
        self.__host = os.environ.get("host")
        self.__user = os.environ.get("username")
        self.__password = os.environ.get("password")
        self.__auth_plugin = os.environ.get('auth_plugin')
        self.__database = os.environ.get("database")
        self.__table_name = "student"
        self.createConnection()
        self.createTable()
        
   def createTable(self):
        """
    Description:
        This method is used to create a table in a database.
    Parameter:
        It takes self as a parameter that contains connection and table name.
       
    """
        try:
            cur = self.__conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS " +
                    self.__table_name + "(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255),phone VARCHAR(13))")
            print("Table has been created successfully")

        except Exception as e:
            logger.error(e)
        
   def insert_data(self):
        """
    Description:
        This method is used for inserting records into the table
    Parameter:
        It takes self as a parameter that contains connection and table name.
       
    """
        try:
            name = input('Enter your name: ')
            address = input('Enter your address:')
            phone = input('Enter your phone number:')
            val = (name,address,phone)
            cur = self.__conn.cursor()
            cur.execute("INSERT INTO "+self.__table_name +" (name, address,phone) VALUES (%s, %s,%s)", val)
            self.__conn.commit()
            print(cur.rowcount,"Records Inserted Successfully")
        
        except Exception as e:
            logger.error(e)
   def fetch_data(self):
        """
    Description:
        This method is used for displaying all records from the database.
    Parameter:
        It takes self as a parameter that contains connection and table name.
       
    """
        try:
            cur = self.__conn.cursor()
            cur.execute("SELECT * FROM " + self.__table_name)
            for row in cur:
                print('Id : ', row[0])
                print('Name : ', row[1])
                print('Address : ', row[2])
                print('Phone Number : ', row[3])

        except Exception as e:
            logger.error(e)   
   def update_data(self):
        """
    Description:
        This method is used for editing and update records of the database.
    Parameter:
        It takes self as a parameter that contains connection and table name.
       
    """
        try:
            id = input('Search by id:')
            name = input('Edit name:')
            address = input('Edit Address:')
            phone = input('Edit Phone Number:')
            cur = self.__conn.cursor()
            cur.execute("UPDATE " + self.__table_name +
                        " SET name = %s,address = %s, phone = %s WHERE id = %s",(name, address, phone, id))
            self.__conn.commit()
            print(cur.rowcount,"Records Updated Successfully")
        
        except Exception as e:
            logger.error(e)  
            
   def delete_data(self):
        """
    Description:
        This method is used for deleting records from the database.
    Parameter:
        It takes self as a parameter that contains connection and table name.
       
    """
        try:
            id = input('Enter user id to delete Record : ')
            cur = self.__conn.cursor()
            cur.execute("DELETE FROM " + self.__table_name +
                        " WHERE id = %s",(id,))
            self.__conn.commit()
            print(cur.rowcount,"Records Deleted successfully")
        
        except Exception as e:
            logger.error(e)
            
    def insert_many(self):
        """
    Description:
        This method is used for inserting multiple records to the database table.
    Parameter:
        It takes self as a parameter that contains connection and table name.

    """
        try:
            val = [("bikash tamang", "kurseong", "9898767634", 21),
                   ("Rahul kharka", "banglore", "7864563345", 22),
                   ("Akash bhutia", "siliguri", "9675465675", 18),
                   ("Sagar sherpa", "Delhi", "9867543873", 23)]
            cur = self.__conn.cursor()
            cur.executemany("INSERT INTO " + self.__table_name + "(name,address,phone,Age) " +
                            "VALUES (%s,%s,%s,%s)", val)
            self.__conn.commit()
            logger.info(cur.rowcount, "Multiple record inserted sucessfully..")

        except Exception as e:
            logger.error(e)  
                             
   def createConnection(self):
        """
    Description:
        This method is used for creating connection with the mysql database.
    Parameter:
        It takes self as a parameter that contains  cretiental details of mysql database.
       
    """
        try:
            conn = connector.connect(
                host=self.__host,
                user=self.__user,
                passwd=self.__password,
                auth_plugin=self.__auth_plugin,
                database=self.__database
            )
            self.__conn = conn
        
        except Exception as e:
            logger.error(e)
