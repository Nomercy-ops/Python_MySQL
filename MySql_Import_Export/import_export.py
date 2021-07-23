"""
@Author: Rikesh Chhetri
@Date: 2021-07-23
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-23 4:03:30
@Title : Program Aim is to use import and exporting of sql file.
"""

import os
import mysql.connector as connector
from LoggerHandler import logger
from dotenv import load_dotenv
load_dotenv('.env')


class ImportExport():
    def __init__(self):
        self.username = os.getenv("DB_USER")
        self.password = os.getenv('DB_PASSWORD')
        self.auth_plugin = os.getenv('AUTH_PLUGIN')
        self.createConnection()

    def createConnection(self):
        """
    Description:
        This method is used for creating connection with the mysql database.
    Parameter:
        It takes self as a parameter.

    """
        try:
            con = connector.connect(
                user = self.username,
                passwd = self.password,
                auth_plugin = self.auth_plugin
                )
            self.conn = con
        except Exception as e:
            logger.error(e)


