import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad,pad




class MyEncrypter(object):
    """
    My class to define different encryter

    Attributes
    ----------
    encrypt_scheme : str
        encrypter type, type in to get relatived encrypter class
        
    Methods
    ----------
    encrypt(content):
        return encrypt value.

    decrypt(content):
        return decrypt value.

    spark_df_encrypt(df, encrypt_col):
        encrypt a spark dataframe column's value.
    
    spark_df_decrypt(df, encrypt_col):
        decrypt a spark dataframe column's value.

    """
    def __init__(self, encrypt_scheme):    
        """
        Constructs all the necessary attributes for MyEncrypter object.

        Parameters
        ----------
            encrypt_scheme : str
                scheme name to get relative encrypt class
        """  
        if encrypt_scheme == 'define_scheme':
            self.encrypter = INVOKE_ENCRYPTER_CLASS_BELOW
        
    def encrypt(self, content):
        return self.encrypter()._encrypt(content)
    def decrypt(self, content):
        return self.encrypter()._decrypt(content)
    def spark_df_encrypt(self, df, encrypt_col):
        return self.encrypter()._spark_encrypt(df,encrypt_col)
    def spark_df_decrypt(self, df, encrypt_col):
        return self.encrypter()._spark_decrypt(df,encrypt_col)

    
class Encrypter(object):
    def __init__(self):
        if os.environ['ENV'] =='dev' or  'prd':
            # construct any function to fit differnet environments
            pass
        else:
            # construct any function to fit differnet environments
            pass
        # construct any function to fit differnet environments


class ECBTypeEncrypter(Encrypter):
    def __init__(self):
        super().__init__()
        _tmp_key = """ define the key here"""
        self._cipher = AES.new(_tmp_key, AES.MODE_ECB)
    def _encrypt(self,content):
        content = content.encode()
        result = self._cipher.encrypt(pad(content, AES.block_size))
        return result
    
    def _decrypt(self, content):
        return unpad(self._cipher.decrypt(content), AES.block_size).decode("utf-8")    
    
    def _spark_encrypt(self, df, encrypt_col):
        _tmp_key = """ define the key here"""       
        for i in encrypt_col:
            df = df.withColumn(i, F.encode(F.col(i),'utf-8'))\
                   .withColumn(i, F.expr(f"aes_encrypt({i}, unbase64('{_tmp_key}'), 'ECB', 'PKCS')"))
        return df

    def _spark_decrypt(self, df, encrypt_col):
        _tmp_key = """ define the key here"""     
        for i in encrypt_col:
            df = df.withColumn(i, F.expr(f"aes_decrypt({i},unbase64('{_tmp_key}'), 'ECB', 'PKCS')"))\
                   .withColumn(i, F.decode(i,'utf-8'))
        return df