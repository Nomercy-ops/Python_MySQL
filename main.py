"""
@Author: Rikesh Chhetri
@Date: 2021-07-21
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-21 10:03:30
@Title : Program Aim is to create a mysql views.
"""
from views.Views import MySqlViews
from LoggerHandler import logger

def menu():
    """
    Description:
        This function is used for calling VIews functions class methods.
       
    """
    try:
        view = MySqlViews()
        view.createView()
        view.displayView()
        view.updateView()
        view.dropView()
    
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    menu()
