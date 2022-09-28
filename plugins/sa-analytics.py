# sa-analytics.py

import json
import sys
import requests

key_list = sys.argv[1]
env_list = sys.argv[2]
keybase64 = 'your own key'
headersAuth = {'Authorization': 'Basic ' + str(keybase64)}

#read all api keys
with open(key_list) as f:
    data = json.load(f)

#read all service accounts
with open(env_list) as sa:
    sas = json.load(sa)

sa_counter = 0
for sa_index in sas:
    serviceaccount = sa_index['id']
    sa_name = sa_index['name']
    # check is service account has an API key
    key_status = 'FALSE'
    for apikey in data:
            key = apikey['key']               
            owner_resource_id = apikey['owner_resource_id']
            # check if service account exists
            if owner_resource_id == serviceaccount:
                key_status = 'TRUE'
                sa_counter +=1
    if key_status != 'TRUE':
            print('Service Account {} with name {} has no  API-KEY : confluent iam service-account delete {} '.format(serviceaccount,sa_name, serviceaccount))

print('End of Service Account analyis: {} service accounts can be deleted '.format(sa_counter))
print('Attention: Before deleting Service Accounts: SA without API Key could be disabled for use. Can be enabled with a new key alignment.')
