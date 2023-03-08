import pyspark.sql.functions as F
from pyspark.sql.types import *

def my_encrypt_func():
    '''
    define encrypt function here
    '''
    pass


def my_udf(dct):
    tmp_dict={}
    if dct:
        for k, v in dct.items():
            if k =='main key':
                tmp_dict[k] = my_encrypt_func(v)
            elif k =='other key':
                tmp_dict[k] = my_encrypt_func(v)

            else:
                tmp_dict[k] = v
        return tmp_dict
    else:
        return dct

n_udf =  F.udf(lambda x: my_udf(x) , MapType(StringType(), StringType()) )