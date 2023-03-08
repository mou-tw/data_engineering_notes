import datetime
import functools


class PipelineProcessError(Exception):
    def __init__(self, table_name, stage, error):
        self.message = f'Pipeline Process Error, table_name:{table_name}, stage:{stage} ,error:{error}'
        super().__init__(self.message)

class MainProcessCls(object):
    _encrypt_columns = []
    _key_columns     = []
    _phone_columns   = []
    before_table_rows= 0
    insert_rows      = 0
    delete_rows      = 0
    
    def __init__(self, table_name):
        self.spark           = replace_spark_here
        self.table_name      = table_name
        self.catalog_name    = replace_catalog_name_here
    
    @staticmethod
    def handle_process_error(stage):
        def exception_handler(func):
            """
            A function wrapper for catching all exceptions
            """
            @functools.wraps(func)
            def inner( *args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    #add teams/slack notification here
                    raise PipelineProcessError(args[0].table_name, stage, error)
            return inner
        return exception_handler 