"""
@Author: Rikesh Chhetri
@Date: 2021-07-21
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-21 10:03:30
@Title : Program Aim is to create a mysql views.
"""

import os
import mysql.connector as connector
from LoggerHandler import logger
from dotenv import load_dotenv
load_dotenv('.env')


class MySqlViews():

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
            
    def createView(self):
        '''
        Description:
            This function creates a view from the staff table.
        Parameter:
            it takes self as parameter.
        '''

        try: 
            cur  = self.conn.cursor()
            cur.execute("CREATE VIEW staff_details AS SELECT staff_name, staff_address, staff_Age FROM Staff")
            logger.info("View has been created successfully")
        
        except Exception as e:
            logger.error(e) 
            
    def displayView(self):
        '''
        Description:
            This function is used to display currently created the view
        Parameter:
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM staff_details")
            result = cur.fetchall()
            logger.info(result)
        
        except Exception as e:
            logger.error(e)
            
    def updateView(self):
        '''
        Description:
            This function is used for updating  the existing view.
        Parameter:
            it takes self as parameter.
        '''

        try:
            cur  = self.conn.cursor()
            cur.execute("ALTER VIEW staff_details AS SELECT Staff_Name, Staff_Address, Monthly_Package FROM Staff")
            logger.info("View has been Updated Successfully")
    
        except Exception as e:
            logger.error(e)
            
            
            
    
    
