"""
@Author: Rikesh Chhetri
@Date: 2021-07-22
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-21 10:03:30
@Title : Program Aim is to use store procedure.
"""

import os
import mysql.connector as connector
from LoggerHandler import logger
from dotenv import load_dotenv
load_dotenv('.env')


class StoreProcedure():

    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.auth_plugin = os.getenv('AUTH_PLUGIN')
        self.database = os.getenv("DB_NAME")
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

    def create_procedures(self):
        '''
        Description:
            This method is used to creates Procedure without Parameter
        Parameter:
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            cur.execute('''CREATE PROCEDURE show_all_customer()
                                    BEGIN
                                    SELECT * FROM CUSTOMER;
                                    END''')
            logger.info("procedure created Successfully")

            cur.execute('''CREATE PROCEDURE show_indian_customer()
                                    BEGIN
                                    SELECT CUST_NAME AS NAME,CUST_COUNTRY AS COUNTRY FROM CUSTOMER WHERE CUST_COUNTRY = 'India';
                                    
                                    END ''')
            logger.info("procedure created Successfully")
        except Exception as e:
            logger.error()
            
    def call_procedure(self):
        '''
        Description:
            This method is used to call a stored procedure.
        Parameter:
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            cur.callproc('show_all_customer')

            for result in cur.stored_results():
                logger.info(result.fetchall())

            cur.callproc('show_indian_customer')
            for result1 in cur.stored_results():
                logger.info(result1.fetchall())
        except Exception as e:
            logger.error(e)
            
            
            


   
