"""
@Author: Rikesh Chhetri
@Date: 2021-07-21
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-21 10:03:30
@Title : Program Aim is to add index to a column of a database table.
"""
from index.Index import Index
from LoggerHandler import logger

def menu():
    """
    Description:
        This function is used for calling index class methods. 
       
    """
    try:
        index = Index()
        index.singleColumnIndex()
        index.compositeIndex()
        index.display_all_index()
        index.search_record()
        index.dropIndex()
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    menu()
