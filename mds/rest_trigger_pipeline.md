```
# Define imports
import msal

# Enter the details of your AAD app registration
client_id = ''
client_secret = ''
authority = 'https://login.microsoftonline.com/'
scope = ['']
# ex: https://dev.azuresynapse.net/.default



# Create an MSAL instance providing the client_id, authority and client_credential parameters
client = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

# First, try to lookup an access token in cache
token_result = client.acquire_token_silent(scope, account=None)

# If the token is available in cache, save it to a variable
if token_result:
    access_token = 'Bearer ' + token_result['access_token']
    print('Access token was loaded from cache')

# If the token is not available in cache, acquire a new one from Azure AD and save it to a variable
if not token_result:
    token_result = client.acquire_token_for_client(scopes=scope)
    access_token = 'Bearer ' + token_result['access_token']
    print('New access token was acquired from Azure AD')


import requests
import json

url = "https://[synapse development endpoint]/pipelines/http_trigger/createRun?api-version=2020-12-01"

payload={}
headers = {
  'Authorization': access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

#return runId
response.text


```