import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def get_kv_secret(secret_name):
    '''
    kv_secret_get[取得key vault內的secret資料]
    Args:
        secret_name ([str]): [想要取得的secret名稱]
    Returns:
        [Alltype] : [secret內的資料回傳內容]
    '''
    if os.environ['ENV'] == 'prd':
        url = ''
    elif os.environ['ENV'] == 'dev':
        url = ''
    tmp_secret = SecretClient(vault_url=url, credential= DefaultAzureCredential())
    return tmp_secret.get_secret(secret_name).value