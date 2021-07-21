"""
@Author: Rikesh Chhetri
@Date: 2021-07-21
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-21 10:03:30
@Title : Program Aim is to perform different types of joins functions.
"""

import os
import mysql.connector as connector
from LoggerHandler import logger
from dotenv import load_dotenv
load_dotenv('.env')


class JoinsFunction():

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
            
    def inner_join(self):
        """
    Description:
        This method selects records that have matching values in both tables.
    Parameter:
        It takes self as a parameter.
       
    """
        try:
            cur = self.conn.cursor()
            cur.execute(
                "SELECT s.id,s.Staff_Name,s.Staff_Age,p.Amount FROM Staff s INNER JOIN Payment p ON s.id = p.Staff_id ")

            result = cur.fetchall()
            for x in result:
                logger.info(x)

        except Exception as e:
            logger.error(e)
            
    def left_join(self):
        """
    Description:
        This method returns all the values from the left table
        and it also includes matching values from right table
        if there are no matching join value it returns NULL.
    Parameter:
        It takes self as a parameter.
       
    """
        try:
            cur = self.conn.cursor()
            cur.execute(
                "SELECT s.id,s.Staff_Name,p.Date,p.Amount FROM Staff s LEFT JOIN Payment p ON s.id = p.Staff_id ")

            result = cur.fetchall()
            for x in result:
                logger.info(x)

        except Exception as e:
            logger.error(e)
            
    def right_join(self):
        """
    Description:
        This method returns all the values from the rows of right table.
        It also includes the matched values from left table
        but if there is no matching in both tables, it returns NULL.
    Parameter:
        It takes self as a parameter.
       
    """
        try:
            cur = self.conn.cursor()
            cur.execute(
                "SELECT s.id,s.Staff_Name,p.Date,p.Amount FROM Staff s RIGHT JOIN Payment p ON s.id = p.Staff_id ")

            result = cur.fetchall()
            for x in result:
                logger.info(x)

        except Exception as e:
            logger.error(e)
            
