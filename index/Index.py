"""
@Author: Rikesh Chhetri
@Date: 2021-07-21
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-21 10:03:30
@Title : Program Aim is to add index to a column of a database table.
"""

import os
import mysql.connector as connector
from LoggerHandler import logger
from dotenv import load_dotenv
load_dotenv('.env')


class Index():

    def __init__(self):
        self.host=os.getenv("DB_HOST")
        self.user=os.getenv("DB_USER")
        self.password =os.getenv("DB_PASSWORD")
        self.auth_plugin=os.getenv('AUTH_PLUGIN')
        self.database=os.getenv("DB_NAME")
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
                host=self.host,
                user=self.user,
                passwd=self.password,
                auth_plugin=self.auth_plugin,
                database=self.database
            )
            self.conn = conn
        
        except Exception as e:
            logger.error(e)
            
    def singleColumnIndex(self):
        '''
        Description:
            This function creates a index on a single column.
        Parameter:
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            cur.execute("CREATE INDEX cust_name_idx ON CUSTOMER(CUST_NAME)")
            logger.info("Index created successfully")

        except Exception as e:
            logger.error(e)
            
            
            
    
    

