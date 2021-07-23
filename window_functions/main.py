"""
@Author: Rikesh Chhetri
@Date: 2021-07-23
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-23 1:03:30
@Title : Program Aim is to use window function
"""
from window_functions.window_function import WindowFunctions
from LoggerHandler import logger

def menu():
    """
    Description:
        This function is used for calling subquery class methods. 
       
    """
    try:
        win_function = WindowFunctions()
        win_function.aggregate_function()
        win_function.analytical_functions_ntile()
        win_function.analytical_functions_lead()
        win_function.rank()
        win_function.dense_rank()
        win_function.percent_rank()
       
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    menu()
