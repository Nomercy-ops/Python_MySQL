"""
@Author: Rikesh Chhetri
@Date: 2021-07-22
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-22 10:03:30
@Title : Program Aim is to use mysql subquery.
"""
from MySql_Subquery.subquery import Subquery
from LoggerHandler import logger

def menu():
    """
    Description:
        This function is used for calling subquery class methods. 
       
    """
    try:
        subquery = Subquery()
        subquery.in_and_where()
        subquery.subquery_with_comparison_operator()
        subquery.subquery_with_notIn()      
        subquery.subquery_with_exists_and_notExists()
        subquery.subqueries_any_all()
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    menu()
