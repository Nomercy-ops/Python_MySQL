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
