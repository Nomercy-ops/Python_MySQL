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
            
    def import_sql_file(self,new_db_name,filename):
        """
        Description:
            This method is used for importing a sql file  by using mysql command.

        Parameter:
        It takes self as a parameter.

        """
        try:
            
            cur = self.conn.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS {}".format(new_db_name))
            logger.info("Database created successfully")
            os.system('mysql -u{} -p{} {} < {}'.format(self.username,self.password,new_db_name,filename))
            logger.info("file imported successfully")
        except Exception as e:
            logger.error(e)
            
    def export_sql_file(self,dbName,filename):
        """
        Description:
            This method is used for exporting a sql file by using mysqldump.

        Parameter:
        It takes self as a parameter.

        """
        try:
        
            os.system('mysqldump -u{} -p{} {} > {}.sql'.format(self.username,self.password,dbName,filename))
        except Exception as e:
            logger.error(e) 
            


            
                
