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
            
    def in_parameter(self):
        '''
        Description:
            This method is used for creating stored procedure
            an calling it by passing parameter with IN parameter.
        Parameter:
            it takes self as parameter.
        '''
        
        try:
            cur = self.conn.cursor()
            cur.execute('''CREATE PROCEDURE limit_customer(IN var1 INT)
                                    BEGIN
                                    SELECT * FROM CUSTOMER LIMIT var1;  
                                    SELECT COUNT(CUST_CODE) AS Total_Customer FROM CUSTOMER; 
                                    END''')
            logger.info("procedure with in parameter created successfully")
        except Exception as e:
            logger.error(e)
            
    def call_in_procedure(self):
        '''
        Description:
            This method is used to call a stored procedure with IN parameter
        Parameter:
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            cur.callproc('limit_customer', [3, ])
            for result in cur.stored_results():
                logger.info(result.fetchall())
        except Exception as e:
            logger.error(e)
            
    def out_parameter(self):
        '''
        Description:
            This method is used for creating stored procedure
            an calling it by passing parameter with OUT parameter.

        Parameter:
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            cur.execute('''CREATE PROCEDURE max_payment_amount(OUT var1 INT)
                                    BEGIN
                                    SELECT MAX(PAYMENT_AMT) INTO var1 FROM CUSTOMER;
                                    END''')
            logger.info("procedure with out parameter created successfully")
        except Exception as e:
            logger.error(e)
            
    def call_out_procedure(self):
        '''
        Description:
            This method is used to call a stored procedure with OUT parameter
        Parameter:
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            result = cur.callproc('max_payment_amount', ['@M'])
            logger.info(result)
        except Exception as e:
            logger.error(e)
            
     def with_inout_parameter(self):
        '''
        Description:
            This method is used for creating stored procedure
            an calling it by passing parameter with INOUT parameter.
        Parameter:
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            cur.execute('''CREATE PROCEDURE display_city(INOUT var1 VARCHAR(255))
                                    BEGIN
                                    SELECT CUST_CITY INTO var1 FROM CUSTOMER WHERE CUST_CODE = "C00017";
                                    END''')
            logger.info("procedure with inout parameter created successfully")

        except Exception as e:
            logger.error(e)
            
    def call_inout_procedure(self):
        '''
        Description:
            This method is used to call a stored procedure with INOUT parameter
        Parameter:
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            result = cur.callproc('display_city', ['C00017'])
            logger.info(result)
        except Exception as e:
            logger.error(e)
            
    def drop_procedure(self):
        '''
        Description:
            This function drops a procedure.
        Parameter:
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            cur.execute("DROP PROCEDURE display_city")
            cur.execute("DROP PROCEDURE limit_customer")
            cur.execute("DROP PROCEDURE max_payment_amount")
            cur.execute("DROP PROCEDURE show_all_customer")
            cur.execute("DROP PROCEDURE show_indian_customer")
            logger.info("Procedure dropped successfully")
        except Exception as e:
            logger.error(e)
 
