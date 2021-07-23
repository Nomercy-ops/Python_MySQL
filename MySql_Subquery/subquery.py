"""
@Author: Rikesh Chhetri
@Date: 2021-07-22
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-22 10:03:30
@Title : Program Aim is to use mysql subquery.
"""

import os
import mysql.connector as connector
from LoggerHandler import logger
from dotenv import load_dotenv
load_dotenv('.env')


class Subquery():

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

    def in_and_where(self):
        '''
        Description:
            This method returns employees who work in offices located in the France.
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            cur.execute(
                '''SELECT firstName,lastName FROM employees  
                WHERE officeCode IN (SELECT officeCode FROM offices WHERE country = 'USA')''')
            result = cur.fetchall()
            for x in result:
                logger.info(x)
        except Exception as e:
            logger.error(e)
            
    def subquery_with_comparison_operator(self):
        '''
        Description:
            This method returns the customer who has the maximum credit limit and  customer having credit limit greater than average limit..
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            cur.execute(
                '''SELECT customerNumber,customerName
                 FROM customers WHERE creditLimit = (SELECT MAX(creditLimit) FROM customers)''')
            result = cur.fetchall()
            logger.info(result)

            cur.execute(
                '''SELECT customerNumber,customerName
                 FROM customers WHERE creditLimit > (SELECT AVG(creditLimit) FROM customers)''')
            result1 = cur.fetchall()
            logger.info(result1)
        except Exception as e:
            logger.error(e)
            
    def subquery_with_notIn(self):
        '''
        Description:
            This method returns customers who have not placed any orders 
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            cur.execute(
                '''SELECT customerName FROM customers 
                WHERE customerNumber NOT IN (SELECT customerNumber FROM orders)''')
            result = cur.fetchall()
            for x in result:
                logger.info(x)
        except Exception as e:
            logger.error(e)

     def subquery_with_exists_and_notExists(self):
        '''
        Description:
            This method returns customers name and city if order details that exists and not exists.
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            cur.execute(
                '''SELECT customerName,city FROM customers C 
                 WHERE EXISTS (SELECT * FROM orders O WHERE C.customerNumber = O.customerNumber)''')
            result = cur.fetchall()
            for x in result:
                logger.info(x)
            
            cur.execute(
                '''SELECT customerName,city FROM customers C 
                 WHERE NOT EXISTS (SELECT * FROM orders O WHERE C.customerNumber = O.customerNumber)''')
            result1 = cur.fetchall()
            for x in result1:
                logger.info(x)
        except Exception as e:
            logger.error(e)

    def subqueries_any_all(self):
        '''
        Description:
            This method is used with comparison operator and 
            ANY will return TRUE when the comparison is TRUE for ANY values 
            ALL will return TRUE when the comparison is TRUE for ALL values 
        Parameter:
            it takes self as parameter.
        '''

        try:
            cur = self.conn.cursor()
            cur.execute('''SELECT  ordernumber,orderdate FROM orders
              WHERE orderNumber > ANY (SELECT orderNumber FROM orderdetails)''')
            result = cur.fetchall()
            for x in result:
                logger.info(x)
            
            cur.execute('''SELECT  ordernumber,orderdate FROM orders
              WHERE orderNumber > ALL (SELECT orderNumber FROM orderdetails)''')
            result1 = cur.fetchall()
            for x in result1:
                logger.info(x)   
        except Exception as e:
            logger.error(e)


        
            

