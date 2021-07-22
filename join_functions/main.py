"""
@Author: Rikesh Chhetri
@Date: 2021-07-21
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-21 10:03:30
@Title : Program Aim is to perform different types of joins functions. 
"""
from join_functions.joins import JoinsFunction
from LoggerHandler import logger

def menu():
    """
    Description:
        This function is used for calling Joins functions class methods.
       
    """
    try:
        join = JoinsFunction()
        join.inner_join()
        join.left_join()
        join.right_join()
    
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    menu()
