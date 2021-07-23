"""
@Author: Rikesh Chhetri
@Date: 2021-07-23
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-23 1:03:30
@Title : Program Aim is to use Window Functions.
"""

import os
import mysql.connector as connector
from LoggerHandler import logger
from dotenv import load_dotenv
load_dotenv('.env')


class WindowFunctions():

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
            
    def aggregate_function(self):
        """
        Description:
            This method will give sum of sale based on given condition with window function.
        """
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT year,product,sale,SUM(sale) OVER(PARTITION BY year) AS total_sale FROM sales")
            result = cur.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(e)

    def analytical_functions_ntile(self):
        """
        Description:
            This method will sort rows in given numbers in ntile() function.
        """
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT year,product,sale, Ntile(3) OVER() AS total_sale FROM sales")
            result = cur.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(e)

    def analytical_functions_lead(self):
        """
        Description:
            This method will read data from next row in given condition in query.
        """
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT year, product,sale, LEAD(sale,1) OVER(ORDER BY year) AS total_sale FROM sales")
            result = cur.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(e)
            
   
    def dense_rank(self):
        """
        Description:
            This method will give dense rank for given column in a condition.
        """
        try:
            cur = self.conn.cursor()
            cur.execute('''SELECT year, product,sale, dense_rank()
             OVER(PARTITION BY year ORDER BY sale) AS 'dense_rank' FROM sales''')
            result = cur.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(e)
            
    def rank(self):
        """
        Description:
            This method will given ranks for specified column in given query.
        """
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT year, product,sale, rank() OVER(PARTITION BY year ORDER BY sale desc) AS 'rank' FROM sales")
            result = cur.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(e)
            
    def percent_rank(self):
        """
        Description:
            This method will given percent rank for specified column in query.
        """
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT year, product,sale, percent_rank() OVER(PARTITION BY product ORDER BY sale) AS 'percent_rank' FROM sales")
            result = cur.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(e)
            

            
            

