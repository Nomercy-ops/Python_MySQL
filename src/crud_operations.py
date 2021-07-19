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
