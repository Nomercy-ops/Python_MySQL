"""
@Author: Rikesh Chhetri
@Date: 2021-07-22
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-21 10:03:30
@Title :  Program Aim is to use store procedure.
"""
from store_proc.store_procedure import StoreProcedure
from LoggerHandler import logger

def menu():
    """
    Description:
        This function is used for calling stored procedure functions class methods.
       
    """
    try:
        store_proc = StoreProcedure()
        store_proc.create_procedures()
        store_proc.call_procedure()
        store_proc.in_parameter()
        store_proc.call_in_procedure()
        store_proc.out_parameter()
        store_proc.call_out_procedure()
        store_proc.with_inout_parameter()
        store_proc.call_inout_procedure()
        store_proc.drop_procedure()
    
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    menu()
