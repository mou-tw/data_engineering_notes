import re

import great_expectations as ge


class GEUnitTestError(Exception):
    def __init__(self, table_name, exceptation):
        self.message = f'Data Quality Check Failed, Table Name:{table_name}, Test Expectation:{exceptation}'
        super().__init__(self.message)


class DatacenterGECls(object):
    def __init__(self, table_name, spark_df):
        self.table_name   = table_name
        self.ge_dataframe = ge.dataset.SparkDFDataset(spark_df)
        self.expect_lst   = [e for e in self.ge_dataframe.__dir__() if e.startswith('expect')]
    
    def __getattr__(self, attr):
        def call_(*args):
            assert attr in self.expect_lst, 'function name error'
            ge_func = getattr(self.ge_dataframe, attr)
            
            if ge_func(*args)['success']:
                return self
            else:
                #add teams/slack notification here
                raise GEUnitTestError(self.table_name, attr )
            
        return call_
    
    def expect_column_values_to_be_of_type(self, col_type_dict):
        for k in col_type_dict.keys():
            asset_col_type=col_type_dict.get(k,'')
            if bool(re.search(string=asset_col_type,pattern='Decimal|Map|Struct|Array')):
                continue
            
            ge_func = getattr(self.ge_dataframe, 'expect_column_values_to_be_of_type')
            ret = ge_func(k, asset_col_type)
            if not ret['success']:
                #add teams/slack notification here
                raise GEUnitTestError(self.table_name, 'expect_column_values_to_be_of_type' )
        return self
        