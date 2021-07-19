"""
@Author: Rikesh Chhetri
@Date: 2021-07-19
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-19 10:03:30
@Title : Program Aim perform CRUD operations and storing data in mysql database. 
"""

from src.crud_operations import CrudOperations
from LoggerHandler import logger

def menu():
    """
    Description:
        This function is used for calling crud operations methods.
        Table name is passed to the init method of crud operation class.
       
    """
    try:
        print("welcome to crud operations")
        crud = CrudOperations()
        crud.insert_data()
    
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    menu()
