# api-key-analytics.py

import json
import sys
import requests

key_list = sys.argv[1]
env_list = sys.argv[2]
keybase64 = 'add your own key'
headersAuth = {'Authorization': 'Basic ' + str(keybase64)}

#read all api keys
with open(key_list) as f:
    data = json.load(f)

#read all environments
with open(env_list) as env:
    envs = json.load(env)


#print(json.dumps(data, indent=2))
for apikey in data:
    key = apikey['key']
    owner_resource_id = apikey['owner_resource_id']
    resource_type = apikey['resource_type']
    resource_id = apikey['resource_id']
    # print('API-Key {} owned by {} for resource {} with ID {}'.format(key, owner_resource_id, resource_type, resource_id))
    # if cloud, then check if user is still there
    if resource_type == 'cloud':
        # check if it is user or service account
        if owner_resource_id[0] =='u':
            url = 'https://api.confluent.cloud/iam/v2/users/{}'.format(owner_resource_id)
            r = requests.get(url, headers=headersAuth)
            #print(owner_resource_id)
            #print(url)
            if r.status_code != 200:
                print('User {} do not exist anymore, please delete API-KEY{} : confluent api-key delete {} '.format(owner_resource_id,key,key))
        else: 
            url = 'https://api.confluent.cloud/iam/v2/service-accounts/{}'.format(owner_resource_id)
            r = requests.get(url, headers=headersAuth)
            #print (r.status_code)
            if r.status_code != 200:
                print('Service Account {} do not exist anymore, please delete API-KEY{} : confluent api-key delete {} '.format(owner_resource_id ,key, key))
    
    elif resource_type == 'kafka':
        kafka_status = 'FALSE'
        for environment in envs:
            envid = environment['id']                
            url = 'https://api.confluent.cloud/cmk/v2/clusters/{}?environment={}'.format(resource_id,envid)
            r = requests.get(url, headers=headersAuth)
            #print (r.status_code)
            if r.status_code == 200:
                kafka_status = 'TRUE'
        
        if kafka_status != 'TRUE':
            print(url)
            print('Kafka cluster {} in environment {} do not exists anymore, please delete API-KEY{} : confluent api-key delete {} '.format(resource_id,envid, key, key))

print('End of API Key analyis')

