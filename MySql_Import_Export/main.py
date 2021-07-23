"""
@Author: Rikesh Chhetri
@Date: 2021-07-23
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-23 4:03:30
@Title : Program Aim is to use import and exporting of sql file.
"""
from MySql_Import_Export.import_export import ImportExport
from LoggerHandler import logger

def menu():
    """
    Description:
        This function is used for calling import export functions
       
    """
    try:
       imp_export = ImportExport()
       dbName = 'Agent'
       filename = 'file'
       importdb_name = 'new_db'
       file_to_import = '/home/rikesh/Import_Export/file.sql'
       imp_export.export_sql_file(dbName,filename)
       imp_export.import_sql_file(importdb_name,file_to_import)
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    menu()
